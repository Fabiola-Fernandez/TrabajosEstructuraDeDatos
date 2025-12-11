import json
from modelo import Nodo

# crear la raiz
raiz = Nodo("root", "carpeta")

# creamos las carpetas y los archivos hijs
carpeta_docs = Nodo("documentos", "carpeta")
archivo_notas = Nodo("notas.txt", "archivo", contenido="Hola mundo")
archivo_foto = Nodo("foto.png", "archivo", contenido="[binary data]")

# hacemos el arbol nosotros por ahora
raiz.agregar_hijo(carpeta_docs)

carpeta_docs.agregar_hijo(archivo_notas)

raiz.agregar_hijo(archivo_foto)

# imprimimos el JSON
json_output = json.dumps(raiz.to_dict(), indent=4)

print("Estructura del Árbol")
print(f"Raíz: {raiz.nombre}")
print(f"  └── {carpeta_docs.nombre}")
print(f"      └── {archivo_notas.nombre}")
print(f"  └── {archivo_foto.nombre}")

print("\n Formato JSON Definido ")
print(json_output)