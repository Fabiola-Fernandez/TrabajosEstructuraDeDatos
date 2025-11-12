def bucket_sort(arr):
    n = len(arr)
    if n <= 0:
        return arr

    # Crear cubetas vacías
    buckets = [[] for _ in range(n)]

    # Colocar elementos en cubetas
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    # Ordenar cada cubeta
    for bucket in buckets:
        bucket.sort()

    # Unir cubetas
    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr

arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Arreglo ordenado:", bucket_sort(arr))
