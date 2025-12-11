import json
from modelo import Nodo

# 1. Creamos la Raíz (Root)
raiz = Nodo("root", "carpeta")

# 2. Creamos carpetas y archivos hijos
carpeta_docs = Nodo("documentos", "carpeta")
archivo_notas = Nodo("notas.txt", "archivo", contenido="Hola mundo")
archivo_foto = Nodo("foto.png", "archivo", contenido="[binary data]")

# 3. Estructuramos el árbol (manual por hoy)
# root -> documentos
raiz.agregar_hijo(carpeta_docs)

# root -> documentos -> notas.txt
carpeta_docs.agregar_hijo(archivo_notas)

# root -> foto.png
raiz.agregar_hijo(archivo_foto)

# 4. Imprimimos el resultado como se vería en el JSON final
json_output = json.dumps(raiz.to_dict(), indent=4)

print("--- Estructura del Árbol (Visual) ---")
print(f"Raíz: {raiz.nombre}")
print(f"  └── {carpeta_docs.nombre}")
print(f"      └── {archivo_notas.nombre}")
print(f"  └── {archivo_foto.nombre}")

print("\n Formato JSON Definido ")
print(json_output)