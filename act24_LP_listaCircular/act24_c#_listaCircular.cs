using System;

class Nodo {
    public int dato;
    public Nodo sig;
    public Nodo(int d) { dato = d; }
}

class Program {
    static void Main() {
        Nodo n1 = new Nodo(1);
        Nodo n2 = new Nodo(2);
        Nodo n3 = new Nodo(3);

        n1.sig = n2;
        n2.sig = n3;
        n3.sig = n1; // circular

        Nodo temp = n1;
        for (int i = 0; i < 6; i++) {
            Console.Write(temp.dato + " ");
            temp = temp.sig;
        }
    }
}
