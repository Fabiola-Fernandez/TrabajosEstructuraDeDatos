import json

from modelo import Nodo, obtener_nodo_por_ruta, eliminar_nodo_en_ruta, mover_nodo_en_ruta, PAPELERA
from modelo import guardar_arbol_a_json, cargar_arbol_desde_json, Trie, construir_trie_inicial



# Ahora acepta 'trie_index' para indexar el nodo al crearlo
def crear_nodo_en_ruta(raiz, ruta_padre, nombre, tipo, contenido="", trie_index=None):
    """Crea un nuevo Nodo y actualiza el Trie si se proporciona"""
    if ruta_padre == "root" or ruta_padre == "/":
        nodo_padre = raiz
    else:
        nodo_padre, _ = obtener_nodo_por_ruta(raiz, ruta_padre)

    if nodo_padre is None:
        print(f"\n[ERROR: CREAR] Ruta padre '{ruta_padre}' no existe")
        return False

    if nodo_padre.tipo != 'carpeta':
        print(f"\n[ERROR: CREAR] El nodo '{ruta_padre}' es un archivo")
        return False
        
    if nodo_padre.buscar_hijo_por_nombre(nombre):
        print(f"\n[ERROR: CREAR] Ya existe '{nombre}' en '{ruta_padre}'.")
        return False
        
    # Creamos y agregamos
    nuevo_nodo = Nodo(nombre, tipo, contenido)
    nodo_padre.agregar_hijo(nuevo_nodo)
    
    # >>> DÍA 5: MANTENIMIENTO DEL TRIE <<<
    if trie_index:
        trie_index.insertar(nombre, nuevo_nodo)

    
    print(f"\n[ÉXITO: CREAR] Se creó '{tipo}' llamado '{nombre}' en '{ruta_padre}'.")
    return True

# Nueva función auxiliar para manejar el renombre y el Trie
def renombrar_nodo_con_trie(raiz, ruta_origen, nuevo_nombre, trie_index=None):
    """Renombra un nodo y actualiza el índice Trie"""
    nodo_a_renombrar, _ = obtener_nodo_por_ruta(raiz, ruta_origen)

    if nodo_a_renombrar is None:
        print(f"\n[ERROR: RENOMBRAR] Nodo '{ruta_origen}' no existe")
        return False
    
    nombre_viejo = nodo_a_renombrar.nombre
    
    
    if trie_index:
        trie_index.eliminar(nombre_viejo, nodo_a_renombrar)
    
    #Renombrar en el árbol
    nodo_a_renombrar.renombrar(nuevo_nombre)
    
    
    if trie_index:
        trie_index.insertar(nuevo_nombre, nodo_a_renombrar)
        
    print(f"[ÉXITO: RENOMBRAR] '{nombre_viejo}' -> '{nuevo_nombre}' (Trie actualizado)")
    return True



# 2. INICIALIZAMOS EL ÍNDICE GLOBAL
INDICE_TRIE = Trie()

# Crear la raiz
raiz = Nodo("root", "carpeta")
# Indexamos la raíz manualmente
INDICE_TRIE.insertar("root", raiz)

# Creamos hijos iniciales
carpeta_docs = Nodo("documentos", "carpeta")
archivo_notas = Nodo("notas.txt", "archivo", contenido="Hola")
archivo_foto = Nodo("foto.png", "archivo", contenido="[binary data]")

# Agregamos al árbol
raiz.agregar_hijo(carpeta_docs)
carpeta_docs.agregar_hijo(archivo_notas)
raiz.agregar_hijo(archivo_foto)

# 3. INDEXAMOS LOS NODOS INICIALES AL TRIE
INDICE_TRIE.insertar("documentos", carpeta_docs)
INDICE_TRIE.insertar("notas.txt", archivo_notas)
INDICE_TRIE.insertar("foto.png", archivo_foto)




print("\n\n" + "="*50)
print("             PRUEBAS DÍAS 2-5: INTEGRACIÓN ")
print("="*50)


print("\n--- PRUEBA 1: BÚSQUEDA Y CREACIÓN (CON TRIE) ---")

# Buscamos en la estructura
nodo_buscado_1, padre_1 = obtener_nodo_por_ruta(raiz, "/documentos/notas.txt")
print(f"Buscando '/documentos/notas.txt': {'ÉXITO' if nodo_buscado_1 else 'FALLO'}")

# Creamos 'logs', PASANDO EL TRIE para que se indexe automático
crear_nodo_en_ruta(raiz, "/", "logs", "carpeta", trie_index=INDICE_TRIE)

# Verificamos si el Trie esta capturando
encontrados = INDICE_TRIE.buscar_por_prefijo("logs")
print(f"Verificación Trie ('logs'): {'ENCONTRADO' if encontrados else 'NO ENCONTRADO'}")


print("\n--- PRUEBA 2: RENOMBRAR  ---")

# Usamos la nueva función que actualiza el Trie
renombrar_nodo_con_trie(raiz, "/documentos", "mis_documentos", trie_index=INDICE_TRIE)

# Verificamos que el nombre viejo no este y el nuevo si este
busq_vieja = INDICE_TRIE.buscar_por_prefijo("documentos")
busq_nueva = INDICE_TRIE.buscar_por_prefijo("mis_documentos")
print(f"Trie busca 'documentos' (debe ser vacio): {len(busq_vieja)}")
print(f"Trie busca 'mis_documentos' (debe encontrar): {len(busq_nueva)}")


print("\n--- PRUEBA 3: ELIMINAR (CON TRIE) ---")

# Pasamos para que elimine la referencia
eliminar_nodo_en_ruta(raiz, "/foto.png", trie_index=INDICE_TRIE)

# Verificamos
busq_foto = INDICE_TRIE.buscar_por_prefijo("foto")
print(f"Trie busca 'foto' (debe ser vacio): {len(busq_foto)}")
print(f"Papelera tiene: {len(PAPELERA)} elementos")


print("\n--- PRUEBA 4: MOVER NODO ---")

ruta_origen_logs = "/logs"
ruta_destino_docs = "/mis_documentos"
mover_nodo_en_ruta(raiz, ruta_origen_logs, ruta_destino_docs)

nodo_nuevo_check, _ = obtener_nodo_por_ruta(raiz, ruta_destino_docs + "/logs")
print(f"Verificar nueva ruta '/mis_documentos/logs': {'ÉXITO' if nodo_nuevo_check else 'FALLO'}")


print("\n--- PRUEBA 5: ALTURA Y TAMAÑO ---")

print(f"Tamaño total: {raiz.calcular_tamano()} (Debe ser 4)")
print(f"Altura: {raiz.calcular_altura()} (Debe ser 3)")


print("\n" + "="*50)
print("             PRUEBA DÍA 4: PERSISTENCIA")
print("="*50)

print("Intentando GUARDAR...")
guardar_arbol_a_json(raiz, "arbol_persistente.json")

print("\nIntentando CARGAR...")
raiz_cargada = cargar_arbol_desde_json("arbol_persistente.json")

if raiz_cargada:
    print("[ÉXITO: CARGAR] Árbol reconstruido.")
    
    print("\n" + "="*50)
    print("        PRUEBA DÍA 5 y 6: AUTOCOMPLETADO ")
    print("="*50)
    
    # creamos un trie nuevo
    NUEVO_TRIE = Trie()
    
    print("Construyendo índice Trie a partir del árbol cargado...")
    construir_trie_inicial(raiz_cargada, NUEVO_TRIE)
    print("[ÉXITO] Índice construido.")
    
    # Probamos autocompletado
    prefijo = "mis"
    resultados = NUEVO_TRIE.buscar_por_prefijo(prefijo)
    
    print(f"\nAutocompletar '{prefijo}':")
    if resultados:
        for r in resultados:
            print(f"  -> Sugerencia: {r.nombre} ({r.tipo})")
            # 
    else:
        print("  -> No se encontraron resultados")

    # Búsqueda de algo interno
    prefijo_2 = "no" # de notas.txt
    resultados_2 = NUEVO_TRIE.buscar_por_prefijo(prefijo_2)
    print(f"\nAutocompletar '{prefijo_2}':")
    print(f"  -> {[r.nombre for r in resultados_2]}")

    print("\n[PROYECTO DÍAS 1-5 COMPLETADO]")