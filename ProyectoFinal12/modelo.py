import uuid
import json
from collections import defaultdict 

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.es_final_de_palabra = [] 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertar(self, nombre_nodo, nodo_objeto):
        node = self.root
        for char in nombre_nodo.lower(): 
            node = node.children[char]
        if nodo_objeto not in node.es_final_de_palabra:
            node.es_final_de_palabra.append(nodo_objeto)

    def eliminar(self, nombre_nodo, nodo_objeto):
        node = self.root
        for char in nombre_nodo.lower():
            if char not in node.children:
                return False 
            node = node.children[char]
        if nodo_objeto in node.es_final_de_palabra:
            node.es_final_de_palabra.remove(nodo_objeto)
            return True
        return False

    def buscar_por_prefijo(self, prefijo):
        node = self.root
        for char in prefijo.lower():
            if char not in node.children:
                return [] 
            node = node.children[char]
        resultados = []
        self._recolectar_nodos(node, resultados)
        return resultados

    def _recolectar_nodos(self, node, resultados):
        resultados.extend(node.es_final_de_palabra)
        for child_node in node.children.values():
            self._recolectar_nodos(child_node, resultados)

# clase nodo
class Nodo:
    def __init__(self, nombre, tipo, contenido=""):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.tipo = tipo
        self.contenido = contenido
        self.hijos = []

    def agregar_hijo(self, nodo):
        if self.tipo == 'carpeta':
            self.hijos.append(nodo)
        else:
            raise Exception("Un archivo no puede tener hijos")

    def to_dict(self):
        return {
            "id": self.id, "nombre": self.nombre, "tipo": self.tipo,
            "contenido": self.contenido, "hijos": [h.to_dict() for h in self.hijos]
        }

    def buscar_hijo_por_nombre(self, nombre_buscado):
        for hijo in self.hijos:
            if hijo.nombre == nombre_buscado: return hijo
        return None
        
    def renombrar(self, nuevo_nombre):
        if not nuevo_nombre: raise ValueError("Nombre vacío")
        self.nombre = nuevo_nombre

    def eliminar_hijo(self, nombre_hijo):
        for i, hijo in enumerate(self.hijos):
            if hijo.nombre == nombre_hijo: return self.hijos.pop(i)
        return None
        
    def calcular_tamano(self):
        return 1 + sum(h.calcular_tamano() for h in self.hijos)

    def calcular_altura(self):
        if not self.hijos: return 1
        return 1 + max(h.calcular_altura() for h in self.hijos)

# crud mas validaciones de los dias

PAPELERA = [] 

def obtener_nodo_por_ruta(raiz, ruta):
    if ruta == "/": return raiz, None
    partes = [p for p in ruta.split('/') if p]
    actual = raiz
    padre = None
    for parte in partes:
        if actual.tipo != 'carpeta': return None, None
        hijo = actual.buscar_hijo_por_nombre(parte)
        if not hijo: return None, None
        padre = actual
        actual = hijo
    return actual, padre

def eliminar_nodo_en_ruta(raiz, ruta, trie_index=None):
    nodo, padre = obtener_nodo_por_ruta(raiz, ruta)
    if not nodo or nodo is raiz: return False
    
    eliminado = padre.eliminar_hijo(nodo.nombre)
    if eliminado:
        if trie_index: trie_index.eliminar(eliminado.nombre, eliminado)
        PAPELERA.append(eliminado)
        print(f" > Eliminado: {ruta}")
        return True
    return False

def mover_nodo_en_ruta(raiz, ruta_origen, ruta_destino):
    """
    [ACTUALIZADO DÍA 10] Incluye validación de movimiento
    """
    nodo_mov, padre_orig = obtener_nodo_por_ruta(raiz, ruta_origen)
    if not nodo_mov:
        print("Error: Origen no existe"); return False
    
    nodo_dest, _ = obtener_nodo_por_ruta(raiz, ruta_destino)
    if not nodo_dest or nodo_dest.tipo != 'carpeta':
        print("Error: Destino inválido"); return False

    
    # Evitar mover una carpeta dentro de sí misma
    clean_orig = ruta_origen.strip('/')
    clean_dest = ruta_destino.strip('/')
    if clean_dest.startswith(clean_orig):
        print(f"\n[ERROR CRÍTICO] Movimiento ilegal: No puedes mover '{clean_orig}' dentro de '{clean_dest}'.")
        return False
    # ---------------------------------------

    if nodo_dest.buscar_hijo_por_nombre(nodo_mov.nombre):
        print("Error: Ya existe ese nombre en destino"); return False

    desconectado = padre_orig.eliminar_hijo(nodo_mov.nombre)
    if desconectado:
        nodo_dest.agregar_hijo(desconectado)
        print(f" > Movido: {ruta_origen} -> {ruta_destino}")
        return True
    return False

def construir_trie_inicial(raiz, trie_index):
    trie_index.insertar(raiz.nombre, raiz)
    for hijo in raiz.hijos:
        construir_trie_inicial(hijo, trie_index)


# peristencia

def dict_to_nodo(data):
    nodo = Nodo(data["nombre"], data["tipo"], data.get("contenido", ""))
    if 'hijos' in data:
        for h in data['hijos']: nodo.hijos.append(dict_to_nodo(h))
    return nodo

def cargar_arbol_desde_json(archivo="estructura_final.json"):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return dict_to_nodo(json.load(f))
    except: return None

def guardar_arbol_a_json(raiz, archivo="estructura_final.json"):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(json.dumps(raiz.to_dict(), indent=4))
        return True
    except Exception as e:
        print(f"Error al guardar: {e}"); return False