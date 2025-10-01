using System;

class HeapSort {
    static void Heapify(int[] arr, int n, int i) {
        int mayor = i;
        int izquierda = 2 * i + 1;
        int derecha = 2 * i + 2;

        if (izquierda < n && arr[izquierda] > arr[mayor])
            mayor = izquierda;

        if (derecha < n && arr[derecha] > arr[mayor])
            mayor = derecha;

        if (mayor != i) {
            int temp = arr[i];
            arr[i] = arr[mayor];
            arr[mayor] = temp;

            Heapify(arr, n, mayor);
        }
    }

    public static void Sort(int[] arr) {
        int n = arr.Length;

        for (int i = n/2 - 1; i >= 0; i--)
            Heapify(arr, n, i);

        for (int i = n-1; i >= 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            Heapify(arr, i, 0);
        }
    }

    static void Main() {
        int[] arr = {12, 11, 13, 5, 6, 7};
        Sort(arr);
        Console.WriteLine("Arreglo ordenado: " + string.Join(" ", arr));
    }
}