def hash_sort(arr):
    # Conjunto elimina duplicados
    unique = set(arr)
    # Ordenar
    return sorted(unique)

arr = [4, 2, 7, 1, 3, 7, 2]
print("Arreglo ordenado:", hash_sort(arr))
