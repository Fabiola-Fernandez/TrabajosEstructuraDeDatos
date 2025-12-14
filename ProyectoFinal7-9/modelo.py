import uuid
import json
from collections import defaultdict 


class TrieNode:
    """Nodo para la estructura Trie"""
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.es_final_de_palabra = [] 

class Trie:
    """
    [Día 5] Implementación de la estructura de datos Trie
    """
    def __init__(self):
        self.root = TrieNode()

    def insertar(self, nombre_nodo, nodo_objeto):
        """Inserta un nombre en el Trie y asocia el objeto Nodo"""
        node = self.root
        for char in nombre_nodo.lower(): 
            node = node.children[char]
        
        if nodo_objeto not in node.es_final_de_palabra:
            node.es_final_de_palabra.append(nodo_objeto)

    def buscar_por_prefijo(self, prefijo):
        """Busca todos los nodos que comienzan con el prefijo"""
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

    def eliminar(self, nombre_nodo, nodo_objeto):
        """[Día 5] Elimina la referencia de un objeto del Trie"""
        node = self.root
        
        for char in nombre_nodo.lower():
            if char not in node.children:
                return False 
            node = node.children[char]
        
        if nodo_objeto in node.es_final_de_palabra:
            node.es_final_de_palabra.remove(nodo_objeto)
            return True
        return False


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
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "contenido": self.contenido,
            "hijos": [hijo.to_dict() for hijo in self.hijos]
        }

    def __repr__(self):
        return f"<{self.tipo}: {self.nombre}>"

    def buscar_hijo_por_nombre(self, nombre_buscado):
        for hijo in self.hijos:
            if hijo.nombre == nombre_buscado:
                return hijo
        return None
        
    def renombrar(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede ser vacío")
        self.nombre = nuevo_nombre

    def eliminar_hijo(self, nombre_hijo):
        for i, hijo in enumerate(self.hijos):
            if hijo.nombre == nombre_hijo:
                nodo_eliminado = self.hijos.pop(i)
                return nodo_eliminado 
        return None
        
    def calcular_tamano(self):
        tamano = 1
        for hijo in self.hijos:
            tamano += hijo.calcular_tamano()
        return tamano

    def calcular_altura(self):
        if not self.hijos:
            return 1
        alturas_hijos = [hijo.calcular_altura() for hijo in self.hijos]
        return 1 + max(alturas_hijos)



PAPELERA = [] 

def obtener_nodo_por_ruta(raiz, ruta):
    if ruta == "/":
        return raiz, None

    partes_ruta = [p for p in ruta.split('/') if p]
    nodo_actual = raiz
    nodo_padre = None

    for nombre_parte in partes_ruta:
        if nodo_actual.tipo != 'carpeta':
            return None, None
        siguiente_nodo = nodo_actual.buscar_hijo_por_nombre(nombre_parte)
        
        if siguiente_nodo is None:
            return None, None
            
        nodo_padre = nodo_actual
        nodo_actual = siguiente_nodo
        
    return nodo_actual, nodo_padre

def eliminar_nodo_en_ruta(raiz, ruta_a_eliminar, trie_index=None):
    """Elimina un nodo"""
    nodo_a_eliminar, nodo_padre = obtener_nodo_por_ruta(raiz, ruta_a_eliminar)

    if nodo_a_eliminar is None:
        print(f"\n[ERROR: ELIMINAR] Ruta '{ruta_a_eliminar}' no existe")
        return False
        
    if nodo_a_eliminar is raiz:
        print("\n[ERROR: ELIMINAR] No se puede eliminar la raíz")
        return False

    nodo_eliminado = nodo_padre.eliminar_hijo(nodo_a_eliminar.nombre)

    if nodo_eliminado:
        if trie_index:
            trie_index.eliminar(nodo_eliminado.nombre, nodo_eliminado)

        PAPELERA.append(nodo_eliminado)
        print(f"\nÉXITO: ELIMINAR Nodo '{ruta_a_eliminar}' enviado a la papelera")
        return True
    return False

def mover_nodo_en_ruta(raiz, ruta_origen, ruta_destino):
    # Buscar origen
    nodo_a_mover, padre_origen = obtener_nodo_por_ruta(raiz, ruta_origen)

    if nodo_a_mover is None:
        print(f"\nERROR: MOVER El nodo de origen '{ruta_origen}' no existe")
        return False
    
    # Buscar destino
    nodo_destino, _ = obtener_nodo_por_ruta(raiz, ruta_destino)

    if nodo_destino is None:
        print(f"\nERROR: MOVER La carpeta de destino '{ruta_destino}' no existe")
        return False

    if nodo_destino.tipo != 'carpeta':
        print(f"\nERROR: MOVER El destino '{ruta_destino}' no es una carpeta")
        return False
        
    if nodo_destino.buscar_hijo_por_nombre(nodo_a_mover.nombre):
        print(f"\nERROR: MOVER ya existe un nodo llamado '{nodo_a_mover.nombre}' en el destino")
        return False

    # Conectar 
    nodo_desconectado = padre_origen.eliminar_hijo(nodo_a_mover.nombre)
    
    if nodo_desconectado:
        nodo_destino.agregar_hijo(nodo_desconectado)
        print(f"\nÉXITO: MOVER Nodo '{ruta_origen}' movido a '{ruta_destino}'.")
        return True
    return False

def construir_trie_inicial(raiz, trie_index):
    """Recorre el árbol recursivamente e inserta todo en el Trie"""
    trie_index.insertar(raiz.nombre, raiz)
    for hijo in raiz.hijos:
        construir_trie_inicial(hijo, trie_index)



def dict_to_nodo(data):
    nodo = Nodo(
        nombre=data["nombre"],
        tipo=data["tipo"],
        contenido=data.get("contenido", "")
    )
    if 'hijos' in data and data['hijos']:
        for hijo_dict in data['hijos']:
            nodo_hijo = dict_to_nodo(hijo_dict)
            nodo.hijos.append(nodo_hijo)
    return nodo

def cargar_arbol_desde_json(nombre_archivo="estructura_final.json"):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos_dict = json.load(archivo)
            raiz_recuperada = dict_to_nodo(datos_dict)
            return raiz_recuperada
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("Error: El archivo JSON no tiene un formato válido")
        return None

def guardar_arbol_a_json(raiz, nombre_archivo="estructura_final.json"):
    try:
        json_output = json.dumps(raiz.to_dict(), indent=4)
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(json_output)
        print(f"\n--- ÉXITO: GUARDADO ---")
        print(f"Los datos se guardaron correctamente en: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return False 