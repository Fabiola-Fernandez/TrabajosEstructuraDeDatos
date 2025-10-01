def heapify(arr, n, i):
    mayor = i
    izquierda = 2*i + 1
    derecha = 2*i + 2

    if izquierda < n and arr[izquierda] > arr[mayor]:
        mayor = izquierda

    if derecha < n and arr[derecha] > arr[mayor]:
        mayor = derecha

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Arreglo ordenado:", arr)