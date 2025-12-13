import json

from modelo import Nodo, obtener_nodo_por_ruta, eliminar_nodo_en_ruta, mover_nodo_en_ruta, PAPELERA 

def crear_nodo_en_ruta(raiz, ruta_padre, nombre, tipo, contenido=""):
    """
    Crea un nuevo Nodo en una ruta específica
    Usa la función obtener_nodo_por_ruta para encontrar el padre
    """
    # crear en la raíz ruta "/"
    if ruta_padre == "root" or ruta_padre == "/":
        nodo_padre = raiz
    else:
        # Buscar el nodo padre donde se quiere crear
        # Usamos '_' para ignorar el padre del nodo padre 
        nodo_padre, _ = obtener_nodo_por_ruta(raiz, ruta_padre)

    if nodo_padre is None:
        print(f"\nERROR: CREAR Ruta padre '{ruta_padre}' no existe")
        return False

    if nodo_padre.tipo != 'carpeta':
        print(f"\nERROR: CREAR El nodo '{ruta_padre}' es un archivo y no puede contener hijos")
        return False
        
    # Verificar que el nombre no exista ya en el padre
    if nodo_padre.buscar_hijo_por_nombre(nombre):
        print(f"\nERROR: CREAR Ya existe un archivo/carpeta con el nombre '{nombre}' en '{ruta_padre}'.")
        return False
        
    # Creamos y agregamos el nuevo nodo
    nuevo_nodo = Nodo(nombre, tipo, contenido)
    nodo_padre.agregar_hijo(nuevo_nodo)
    print(f"\nÉXITO: CREAR Se creó '{tipo}' llamado '{nombre}' en la ruta '{ruta_padre}'.")
    return True


# crear la raiz
raiz = Nodo("root", "carpeta")

# creamos las carpetas y los archivos hijos
carpeta_docs = Nodo("documentos", "carpeta")
archivo_notas = Nodo("notas.txt", "archivo", contenido="Hola")
archivo_foto = Nodo("foto.png", "archivo", contenido="[binary data]")

raiz.agregar_hijo(carpeta_docs)
carpeta_docs.agregar_hijo(archivo_notas)
raiz.agregar_hijo(archivo_foto)


print("\n\n" + "="*50)
print("             PRUEBAS DÍA 2-3: OPERACIONES BÁSICAS")
print("="*50)


### PRUEBA 4 ELIMINAR NODO CON PAPELERA
print("\n--- PRUEBA 4: ELIMINAR (rm) ---")


eliminar_nodo_en_ruta(raiz, "/foto.png")

# Verificar que el nodo eliminado está en la Papelera
print(f"Nodos en Papelera: {len(PAPELERA)} (Debe ser 1)")
print(f"Último nodo en Papelera: {PAPELERA[0].nombre} (Debe ser 'foto.png')")

# 4c. Verificar que el archivo eliminado ya no existe en el árbol
nodo_eliminado_check, _ = obtener_nodo_por_ruta(raiz, "/foto.png")
print(f"Verificar '/foto.png': {'FALLO ' if nodo_eliminado_check is None else 'ERROR'}")



print("\n--- PRUEBA 5: MOVER NODO ---")

# Mover la carpeta 'logs' a 'mis_documentos' 
ruta_origen_logs = "/logs"
ruta_destino_docs = "/mis_documentos"
mover_nodo_en_ruta(raiz, ruta_origen_logs, ruta_destino_docs)

# buscar el nodo en la nueva ruta
nodo_nuevo_check, _ = obtener_nodo_por_ruta(raiz, ruta_destino_docs + "/logs")
print(f"Verificar nueva ruta '/mis_documentos/logs': {'ÉXITO' if nodo_nuevo_check else 'FALLO'}")


### ALTURA Y TAMAÑO
print("\n--- PRUEBA 6: ALTURA Y TAMAÑO ---")

# Calculamos el tamaño y la altura del árbol después de todos los cambios

print(f"Tamaño total del árbol: {raiz.calcular_tamano()} (Debe ser 5)")
print(f"Altura del árbol: {raiz.calcular_altura()} (Debe ser 3)")


### PRUEBA FINAL una nueva estructura
print("\n" + "="*50)
print("ESTRUCTURA FINAL DESPUÉS DE PRUEBAS")
print("="*50)

# Imprimimos el nuevo JSON para ver que los cambios 
json_output_final = json.dumps(raiz.to_dict(), indent=4)
print(json_output_final)