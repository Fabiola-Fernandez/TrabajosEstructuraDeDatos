import uuid
import json


class Nodo:
    def __init__(self, nombre, tipo, contenido=""):
        # Generamos un ID único random
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        # para el tipo de carpeta o archivo
        self.tipo = tipo
        # las carpetas vasias y los arhivos con el contenido
        self.contenido = contenido
        # lista de hijos
        self.hijos = []

    def agregar_hijo(self, nodo):
        """Método para conectar nodos manualmente"""
        if self.tipo == 'carpeta':
            self.hijos.append(nodo)
        else:
            raise Exception("Un archivo no puede tener hijos")

    def to_dict(self):
        """
        Día 1 Convierte el nodo y sus hijos
        """
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
        """Día 2 Busca un nodo hijo directo"""
        for hijo in self.hijos:
            if hijo.nombre == nombre_buscado:
                return hijo
        return None
        
    def renombrar(self, nuevo_nombre):
        """Día 2 Cambia el nombre del nodo"""
        if not nuevo_nombre:
            raise ValueError("El nombre no puede ser vacío")
        self.nombre = nuevo_nombre
        # Lo hacemos en la funcion prinicipal para no saturar

    def eliminar_hijo(self, nombre_hijo):
        """
        Día 2 Elimina un hijo directo por su nombre
        Retorna el Nodo eliminado
        """
        for i, hijo in enumerate(self.hijos):
            if hijo.nombre == nombre_hijo:
                # Usamos pop(i) para eliminar por índice
                nodo_eliminado = self.hijos.pop(i)
                return nodo_eliminado 
        return None
        
    def calcular_tamano(self):
        """
        Día 2 Calcula el número total de nodos
        """
        tamano = 1
        for hijo in self.hijos:
            tamano += hijo.calcular_tamano()
        return tamano

    def calcular_altura(self):
        """
        Día 2 Calcula la altura del árbol
        """
        if not self.hijos:
            return 1
        
        alturas_hijos = [hijo.calcular_altura() for hijo in self.hijos]
        return 1 + max(alturas_hijos)



# Día 2 La papelera temporal es una lista 
PAPELERA = [] 

def obtener_nodo_por_ruta(raiz, ruta):
    """
    Día 3 Busca un nodo en el árbol dada una ruta completa
    Retorna 
    """
    if ruta == "/":
        return raiz, None

    # Limpiar la ruta dividir por '/' y filtrar elementos vacios
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

def eliminar_nodo_en_ruta(raiz, ruta_a_eliminar):
    """
    Día 2 Elimina un nodo del árbol y lo envia a la Papelera 
    """
    nodo_a_eliminar, nodo_padre = obtener_nodo_por_ruta(raiz, ruta_a_eliminar)

    if nodo_a_eliminar is None:
        print(f"\n[ERROR: ELIMINAR] Ruta '{ruta_a_eliminar}' no existe")
        return False
        
    if nodo_a_eliminar is raiz:
        print("\n[ERROR: ELIMINAR] No se puede eliminar la raíz")
        return False

    nodo_eliminado = nodo_padre.eliminar_hijo(nodo_a_eliminar.nombre)

    if nodo_eliminado:
        PAPELERA.append(nodo_eliminado)
        print(f"\nÉXITO: ELIMINAR Nodo '{ruta_a_eliminar}' enviado a la Papelera")
        return True
    return False

def mover_nodo_en_ruta(raiz, ruta_origen, ruta_destino):
    """
    Día 2 Mueve un nodo de una ubicación a otra
    """
    nodo_a_mover, padre_origen = obtener_nodo_por_ruta(raiz, ruta_origen)

    if nodo_a_mover is None:
        print(f"\nERROR: MOVER El nodo de origen '{ruta_origen}' no existe")
        return False
    
    nodo_destino, _ = obtener_nodo_por_ruta(raiz, ruta_destino)

    if nodo_destino is None:
        print(f"\nERROR: MOVER La carpeta de destino '{ruta_destino}' no existe")
        return False

    if nodo_destino.tipo != 'carpeta':
        print(f"\nERROR: MOVER El destino '{ruta_destino}' no es una carpeta")
        return False
        
    if nodo_destino.buscar_hijo_por_nombre(nodo_a_mover.nombre):
        print(f"\nERROR: MOVER Ya existe un nodo llamado '{nodo_a_mover.nombre}' en el destino")
        return False

    # Conectar
    nodo_desconectado = padre_origen.eliminar_hijo(nodo_a_mover.nombre)
    
    if nodo_desconectado:
        nodo_destino.agregar_hijo(nodo_desconectado)
        print(f"\nÉXITO: MOVER Nodo '{ruta_origen}' movido a '{ruta_destino}'.")
        return True
    
    return False


# cargar y guardar
def dict_to_nodo(data):
    """
    Día 4 Función auxiliar para convertir diccionario JSON a objeto
    """
    nodo = Nodo(
        nombre=data["nombre"],
        tipo=data["tipo"],
        contenido=data.get("contenido", "")
    )
    # Mantener el ID original si fuera necesario

    
    if 'hijos' in data and data['hijos']:
        for hijo_dict in data['hijos']:
            nodo_hijo = dict_to_nodo(hijo_dict)
            nodo.hijos.append(nodo_hijo)

    return nodo

def cargar_arbol_desde_json(nombre_archivo="estructura_final.json"):
    """
    Día 4 Función principal que lee el archivo y reconstruye el árbol.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos_dict = json.load(archivo)
            raiz_recuperada = dict_to_nodo(datos_dict)
            return raiz_recuperada
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        return None
    except json.JSONDecodeError:
        print("Error: El archivo JSON no tiene un formato válido")
        return None

def guardar_arbol_a_json(raiz, nombre_archivo="estructura_final.json"):
    """
    Día 4 Función principal que serializa el árbol y lo guarda
    """
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