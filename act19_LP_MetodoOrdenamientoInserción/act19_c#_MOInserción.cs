using System;

class Program {
    static void Main() {
        int[] arr = {5, 2, 9, 1, 5, 6};
        int n = arr.Length;

        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            // Mueve los elementos mayores que "key" una posición adelante
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }

        Console.WriteLine("Arreglo ordenado: " + string.Join(", ", arr));
    }
}
