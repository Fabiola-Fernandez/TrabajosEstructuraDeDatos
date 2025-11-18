using System;
using System.Collections.Generic;

class Program {
    static void Main() {
        List<int> lista = new List<int>() {1, 2, 3};

        lista.Add(4);

        foreach (int n in lista)
            Console.Write(n + " ");
    }
}
