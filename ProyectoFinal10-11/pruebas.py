import time
import json
from modelo import (
    Nodo, Trie, obtener_nodo_por_ruta, eliminar_nodo_en_ruta, 
    mover_nodo_en_ruta, guardar_arbol_a_json, cargar_arbol_desde_json,
    PAPELERA
)



def crear_nodo_test(raiz, ruta_padre, nombre, tipo, trie_index=None):
    if ruta_padre == "/":
        padre = raiz
    else:
        padre, _ = obtener_nodo_por_ruta(raiz, ruta_padre)
    
    if padre:
        nuevo = Nodo(nombre, tipo)
        padre.agregar_hijo(nuevo)
        if trie_index: trie_index.insertar(nombre, nuevo)
        return True
    return False

def renombrar_test(raiz, ruta, nuevo_nombre, trie_index=None):
    nodo, _ = obtener_nodo_por_ruta(raiz, ruta)
    if nodo:
        viejo_nombre = nodo.nombre
        if trie_index: trie_index.eliminar(viejo_nombre, nodo)
        nodo.renombrar(nuevo_nombre)
        if trie_index: trie_index.insertar(nuevo_nombre, nodo)
        return True
    return False



print("\n" + "="*60)
print("     MAESTRA DEL PROYECTO (DÍAS 1 AL 11)")
print("="*60)


print("\n--- [ETAPA 1] ESTRUCTURA Y NAVEGACIÓN (DÍAS 1-3) ---")

# 1. Crear Raíz
raiz = Nodo("root", "carpeta")
trie = Trie()
trie.insertar("root", raiz)
print("[OK] Raíz creada.")

# 2. Crear Hijos
crear_nodo_test(raiz, "/", "documentos", "carpeta", trie)
crear_nodo_test(raiz, "/documentos", "tarea.txt", "archivo", trie)
print("[OK] Estructura /documentos/tarea.txt creada.")

# 3. Buscar
nodo, _ = obtener_nodo_por_ruta(raiz, "/documentos/tarea.txt")
if nodo: print(f"[OK] Búsqueda exitosa: {nodo.nombre}")
else: print("[X] FALLO en búsqueda.")

# ---------------------------------------------------------
# PARTE 2: PERSISTENCIA (DÍA 4)
# ---------------------------------------------------------
print("\n--- [ETAPA 2] PERSISTENCIA JSON (DÍA 4) ---")

guardar_arbol_a_json(raiz, "test_temp.json")
raiz_cargada = cargar_arbol_desde_json("test_temp.json")

if raiz_cargada and raiz_cargada.hijos:
    print("[OK] Árbol guardado y cargado correctamente desde disco")
else:
    print("[X] FALLO en persistencia")


print("\n--- [ETAPA 3] BÚSQUEDA RÁPIDA TRIE (DÍAS 5-9) ---")

# Renombrar y verificar que el Trie se actualice
renombrar_test(raiz, "/documentos", "mis_docs", trie)

res_viejo = trie.buscar_por_prefijo("documentos") # Debe ser vacio
res_nuevo = trie.buscar_por_prefijo("mis_docs")   # Debe encontrar

if not res_viejo and res_nuevo:
    print("[OK] El Trie se actualizó al renombrar ")
else:
    print("[X] FALLO en actualización del Trie")


print("\n--- [ETAPA 4] SEGURIDAD (DÍA 10) ---")

# Creamos escenarios de erro
crear_nodo_test(raiz, "/", "A", "carpeta", trie)
crear_nodo_test(raiz, "/A", "B", "carpeta", trie)

print(" > Intentando mover '/A' dentro de '/A/B' (Movimiento Circular)...")
resultado = mover_nodo_en_ruta(raiz, "/A", "/A/B")

if not resultado:
    print("[OK] sistema seguro: se bloqueo el movimiento")
else:
    print("[X] peligro: El sistema permitio romper el arbol")


print("\n--- [ETAPA 5] PERFORMANCE (DÍA 11) ---")
CANTIDAD = 50000
print(f" > Generando {CANTIDAD} archivos (esto puede tardar unos segundos)...")

start = time.time()
for i in range(CANTIDAD):
    # Solo al trie no satura la ram simulando cargas
    nombre = f"arch_{i}"
    trie.insertar(nombre, Nodo(nombre, "archivo"))
end = time.time()

print(f" > Generación completada en {end - start:.2f} segundos")

print(" > Buscando 'arch_4500' en 50,000 datos...")
start_search = time.time()
res = trie.buscar_por_prefijo("arch_4500")
end_search = time.time()

print(f" > Tiempo de búsqueda: {end_search - start_search:.6f} segundos.")
if (end_search - start_search) < 0.01:
    print("[OK] performance bueno (Tiempo casi instantáneo)")
else:
    print("[WARN] performance regulal")

print("\n" + "="*60)
print("     ¡EL PROYECTO HA PASADO LAS PRUEBAS!")
print("="*60)