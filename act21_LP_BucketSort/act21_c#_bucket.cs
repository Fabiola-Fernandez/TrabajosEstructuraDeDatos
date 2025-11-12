using System;
using System.Collections.Generic;

class BucketSort {
    static void Sort(float[] arr) {
        int n = arr.Length;
        if (n <= 0) return;

        List<float>[] buckets = new List<float>[n];
        for (int i = 0; i < n; i++)
            buckets[i] = new List<float>();

        // Colocar elementos en cubetas
        foreach (float num in arr) {
            int index = (int)(num * n);
            buckets[index].Add(num);
        }

        // Ordenar cada cubeta
        for (int i = 0; i < n; i++)
            buckets[i].Sort();

        // Unir cubetas
        int idx = 0;
        foreach (List<float> bucket in buckets)
            foreach (float num in bucket)
                arr[idx++] = num;
    }

    static void Main() {
        float[] arr = {0.78f, 0.17f, 0.39f, 0.26f, 0.72f, 0.94f, 0.21f, 0.12f, 0.23f, 0.68f};
        Sort(arr);

        Console.WriteLine("Arreglo ordenado:");
        foreach (float num in arr)
            Console.Write(num + " ");
    }
}
