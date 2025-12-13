import json

from modelo import Nodo, obtener_nodo_por_ruta, eliminar_nodo_en_ruta, mover_nodo_en_ruta, PAPELERA
from modelo import guardar_arbol_a_json, cargar_arbol_desde_json


def crear_nodo_en_ruta(raiz, ruta_padre, nombre, tipo, contenido=""):
    """
    Crea un nuevo Nodo en una ruta específica
    """
    # crear en la raíz ruta "/"
    if ruta_padre == "root" or ruta_padre == "/":
        nodo_padre = raiz
    else:
        # Buscar el nodo padre donde se quiere crear
        nodo_padre, _ = obtener_nodo_por_ruta(raiz, ruta_padre)

    if nodo_padre is None:
        print(f"\n[ERROR: CREAR] Ruta padre '{ruta_padre}' no existe")
        return False

    if nodo_padre.tipo != 'carpeta':
        print(f"\n[ERROR: CREAR] El nodo '{ruta_padre}' es un archivo y no puede contener hijos")
        return False
        
    # Verificar que el nombre no exista ya en el padre
    if nodo_padre.buscar_hijo_por_nombre(nombre):
        print(f"\n[ERROR: CREAR] Ya existe un archivo/carpeta con el nombre '{nombre}' en '{ruta_padre}'.")
        return False
        
    # Creamos y agregamos el nuevo nodo
    nuevo_nodo = Nodo(nombre, tipo, contenido)
    nodo_padre.agregar_hijo(nuevo_nodo)
    print(f"\n[ÉXITO: CREAR] Se creó '{tipo}' llamado '{nombre}' en la ruta '{ruta_padre}'.")
    return True



# crear la raiz
raiz = Nodo("root", "carpeta")
carpeta_docs = Nodo("documentos", "carpeta")
archivo_notas = Nodo("notas.txt", "archivo", contenido="Hola")
archivo_foto = Nodo("foto.png", "archivo", contenido="[binary data]")

raiz.agregar_hijo(carpeta_docs)
carpeta_docs.agregar_hijo(archivo_notas)
raiz.agregar_hijo(archivo_foto)


print("\n\n" + "="*50)
print("             PRUEBAS DÍAS 2-3: OPERACIONES BÁSICAS")
print("="*50)


### busqueda y creacion de datos 
print("\n--- PRUEBA 1: BÚSQUEDA Y CREACIÓN INICIAL ---")

# Buscamos para confirmar que la estructura inicial está bien
nodo_buscado_1, padre_1 = obtener_nodo_por_ruta(raiz, "/documentos/notas.txt")
print(f"Buscando '/documentos/notas.txt': {'ÉXITO' if nodo_buscado_1 else 'FALLO'}")

# Creamos la carpeta logs necesaria para la prueba de MOVER
crear_nodo_en_ruta(raiz, "/", "logs", "carpeta")


print("\n--- PRUEBA 2: RENOMBRAR ---")


nodo_a_renombrar, _ = obtener_nodo_por_ruta(raiz, "/documentos")
if nodo_a_renombrar:
    nodo_a_renombrar.renombrar("mis_documentos")
    print(f"[ÉXITO: RENOMBRAR] Documentos -> {nodo_a_renombrar.nombre}")
    
# Verificamos que el nodo con el nombre viejo ya no se encuentra
nodo_viejo = obtener_nodo_por_ruta(raiz, "/documentos")
print(f"Verificar ruta vieja '/documentos': {'FALLO (Esperado)' if nodo_viejo[0] is None else 'ERROR'}")


### eliminamos nodo con papelera
print("\n--- PRUEBA 3: ELIMINAR ---")

eliminar_nodo_en_ruta(raiz, "/foto.png")

# Verificamos la papelera
print(f"Nodos en Papelera: {len(PAPELERA)} (Debe ser 1)")
print(f"Último nodo en Papelera: {PAPELERA[0].nombre} (Debe ser 'foto.png')")

# Verificamos que el archivo eliminado ya no existe en el arbol
nodo_eliminado_check, _ = obtener_nodo_por_ruta(raiz, "/foto.png")
print(f"Verificar '/foto.png': {'FALLO (Esperado)' if nodo_eliminado_check is None else 'ERROR'}")


print("\n--- PRUEBA 4: MOVER NODO ---")


ruta_origen_logs = "/logs"
ruta_destino_docs = "/mis_documentos"
mover_nodo_en_ruta(raiz, ruta_origen_logs, ruta_destino_docs)


nodo_nuevo_check, _ = obtener_nodo_por_ruta(raiz, ruta_destino_docs + "/logs")
print(f"Verificar nueva ruta '/mis_documentos/logs': {'ÉXITO' if nodo_nuevo_check else 'FALLO'}")


### ALTURA Y TAMAÑO
print("\n--- PRUEBA 5: ALTURA Y TAMAÑO ---")


print(f"Tamaño total del árbol: {raiz.calcular_tamano()} (Debe ser 4)")
print(f"Altura del árbol: {raiz.calcular_altura()} (Debe ser 3)")

print("\n" + "="*50)
print("ESTRUCTURA FINAL DESPUÉS DE PRUEBAS (JSON)")
print("="*50)

json_output_final = json.dumps(raiz.to_dict(), indent=4)
print(json_output_final)


print("\n\n" + "="*50)
print("             PRUEBA DÍA 4: GUARDAR Y CARGAR")
print("="*50)

# Gurada la raíz modificada
print("Intentando GUARDAR el árbol actual")
guardar_arbol_a_json(raiz, "arbol_persistente.json")

# Carga el arbol desde el archivo guardado
print("\nIntentando CARGAR el árbol desde 'arbol_persistente.json'")
raiz_cargada = cargar_arbol_desde_json("arbol_persistente.json")

if raiz_cargada:
    print("\n[ÉXITO: CARGAR] Árbol reconstruido correctamente desde el disco.")
    
   
    tamano_cargado = raiz_cargada.calcular_tamano()
    nodo_logs_cargado, _ = obtener_nodo_por_ruta(raiz_cargada, "/mis_documentos/logs")
    
    print(f"  > Tamaño verificado: {tamano_cargado} (Esperado: 4)")
    print(f"  > Nodo movido verificado: {'SÍ' if nodo_logs_cargado else 'NO'}")
    
    print("\n[DÍA 4 COMPLETADO]")