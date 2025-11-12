using System;
using System.Collections.Generic;
using System.Linq;

class HashSort {
    static void Main() {
        int[] arr = {4, 2, 7, 1, 3, 7, 2};

        var sorted = new SortedSet<int>(arr); // elimina duplicados y ordena

        Console.WriteLine("Arreglo ordenado sin duplicados:");
        foreach (var num in sorted)
            Console.Write(num + " ");
    }
}
