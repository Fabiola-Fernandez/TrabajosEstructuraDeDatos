using System;

class Nodo {
    public int dato;
    public Nodo sig;
    public Nodo(int d) { dato = d; }
}

class ListaCircular {
    Nodo cabeza;

    public void Insertar(int d) {
        Nodo nuevo = new Nodo(d);

        if (cabeza == null) {
            cabeza = nuevo;
            nuevo.sig = cabeza;
        } else {
            Nodo temp = cabeza;
            while (temp.sig != cabeza)
                temp = temp.sig;

            temp.sig = nuevo;
            nuevo.sig = cabeza;
        }
    }

    public void Recorrer() {
        if (cabeza == null) return;

        Nodo temp = cabeza;
        do {
            Console.Write(temp.dato + " ");
            temp = temp.sig;
        } while (temp != cabeza);
    }
}

class Program {
    static void Main() {
        ListaCircular lista = new ListaCircular();
        lista.Insertar(1);
        lista.Insertar(2);
        lista.Insertar(3);

        lista.Recorrer();
    }
}
