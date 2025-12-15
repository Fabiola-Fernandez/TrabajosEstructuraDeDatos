import os
import sys

from modelo import (
    Nodo, Trie, cargar_arbol_desde_json, guardar_arbol_a_json, 
    construir_trie_inicial, obtener_nodo_por_ruta, 
    eliminar_nodo_en_ruta, mover_nodo_en_ruta
)


ARBOL = None        
INDICE_TRIE = None  
RUTA_ACTUAL = "/"   
NODO_ACTUAL = None  


# Ruta

def inicializar_sistema():
    global ARBOL, INDICE_TRIE, NODO_ACTUAL
    print("--- INICIANDO SISTEMA DE ARCHIVOS ---")
    
    # arbol de persistencia
    ARBOL = cargar_arbol_desde_json("arbol_persistente.json")
    
    # si no existe crea nuevo
    if not ARBOL:
        print(" > No se encontró 'arbol_persistente.json'. Creando nuevo sistema.")
        ARBOL = Nodo("root", "carpeta")
    else:
        print(" > Sistema cargado correctamente")


    print(" > Construyendo índice de búsqueda...")
    INDICE_TRIE = Trie()
    construir_trie_inicial(ARBOL, INDICE_TRIE)
    
    # Iniciar en la raíz
    NODO_ACTUAL = ARBOL

def resolver_ruta_absoluta(argumento_ruta):
    """Convierte una ruta relativa """
    if not argumento_ruta:
        return RUTA_ACTUAL
        
    if argumento_ruta.startswith("/"):
        return argumento_ruta 
    
    # concatenar
    if RUTA_ACTUAL == "/":
        return f"/{argumento_ruta}"
    else:
        return f"{RUTA_ACTUAL}/{argumento_ruta}"


def cmd_ls():
    """Listar contenido."""
    print(f"\nCarpeta: {RUTA_ACTUAL}")
    if not NODO_ACTUAL.hijos:
        print("  (vacío)")
        return
    for hijo in NODO_ACTUAL.hijos:
        tipo = "<DIR> " if hijo.tipo == 'carpeta' else "<FILE>"
        print(f"  {tipo}  {hijo.nombre}")

def cmd_cd(nombre_carpeta):
    """Navegar a una carpeta"""
    global RUTA_ACTUAL, NODO_ACTUAL
    
    if not nombre_carpeta:
        return # No hacer nada si no escriben nada
        
    if nombre_carpeta == "..":
        
        print("Navegando al inicio ")
        RUTA_ACTUAL = "/"
        NODO_ACTUAL = ARBOL
        return

    ruta_destino = resolver_ruta_absoluta(nombre_carpeta)
    nodo_dest, _ = obtener_nodo_por_ruta(ARBOL, ruta_destino)
    
    if nodo_dest and nodo_dest.tipo == 'carpeta':
        RUTA_ACTUAL = ruta_destino
        NODO_ACTUAL = nodo_dest
    else:
        print(f"Error: '{nombre_carpeta}' no existe o no es carpeta")

def cmd_crear(nombre, tipo, contenido=""):
    """Logica compartida para mkdir y touch"""
    #verifica los duplicados en el nodo actual
    if NODO_ACTUAL.buscar_hijo_por_nombre(nombre):
        print(f"Error: Ya existe '{nombre}' aqui")
        return

    # Crea el nodo
    nuevo = Nodo(nombre, tipo, contenido)
    NODO_ACTUAL.agregar_hijo(nuevo)
    
    # Actualiza Trie
    INDICE_TRIE.insertar(nombre, nuevo)
    print(f"Se creó {tipo}: {nombre}")

def cmd_rm(nombre):
    """Eliminar archivo o carpeta"""
    ruta_completa = resolver_ruta_absoluta(nombre)
    # usamos modelo porque usa el trie
    eliminar_nodo_en_ruta(ARBOL, ruta_completa, trie_index=INDICE_TRIE)

def cmd_mv(origen, destino):
    """Mover un nodo"""
    ruta_orig_abs = resolver_ruta_absoluta(origen)
    ruta_dest_abs = resolver_ruta_absoluta(destino)
    mover_nodo_en_ruta(ARBOL, ruta_orig_abs, ruta_dest_abs)

def cmd_search(prefijo):
    """(Día 9) Buscar usando el Trie"""
    resultados = INDICE_TRIE.buscar_por_prefijo(prefijo)
    print(f"\nResultados de búsqueda para '{prefijo}':")
    if not resultados:
        print("  No se encontraron ")
    else:
        for nodo in resultados:
            print(f"  - {nodo.nombre} ({nodo.tipo})")


def iniciar_consola():
    inicializar_sistema()
    
    print("\n¡Bienvenido a tu File System en Python!")
    print("Escribe 'help' para ver comandos\n")

    while True:
        try:
            entrada = input(f"user@{RUTA_ACTUAL} $ ").strip()
            
            if not entrada: continue
            
            partes = entrada.split()
            comando = partes[0].lower()
            args = partes[1:] 

            if comando == "exit":
                guardar_arbol_a_json(ARBOL, "arbol_persistente.json")
                print("Guardando cambios... ")
                break
            
            elif comando == "help":
                print("\n--- AYUDA ---")
                print("  ls                  Listar directorio actual")
                print("  cd <carpeta>        Entrar a carpeta (.. para root)")
                print("  mkdir <nombre>      Crear carpeta")
                print("  touch <nombre>      Crear archivo")
                print("  rm <nombre>         Eliminar")
                print("  mv <orig> <dest>    Mover")
                print("  search <texto>      Buscar por prefijo (Trie)")
                print("  exit                Guardar y salir")

            elif comando == "ls":
                cmd_ls()

            elif comando == "cd":
                if len(args) < 1: print("Uso: cd <carpeta>")
                else: cmd_cd(args[0])

            elif comando == "mkdir":
                if len(args) < 1: print("Uso: mkdir <nombre>")
                else: cmd_crear(args[0], "carpeta")

            elif comando == "touch":
                if len(args) < 1: print("Uso: touch <nombre>")
                else: cmd_crear(args[0], "archivo", contenido="Archivo vacío")

            elif comando == "rm":
                if len(args) < 1: print("Uso: rm <nombre>")
                else: cmd_rm(args[0])

            elif comando == "mv":
                if len(args) < 2: print("Uso: mv <origen> <destino>")
                else: cmd_mv(args[0], args[1])

            elif comando == "search":
                if len(args) < 1: print("Uso: search <prefijo>")
                else: cmd_search(args[0])
            
            else:
                print("Comando desconocido")

        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    iniciar_consola()