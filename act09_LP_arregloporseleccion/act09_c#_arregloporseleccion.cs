using System;

class Program {
    static void SelectionSort(int[] arr) {
        int n = arr.Length;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
    }

    static void Main() {
        int[] arr = {15, 12, 14, 16, 13};
        SelectionSort(arr);
        Console.WriteLine("Arreglo ordenado: " + string.Join(" ", arr));
    }
}