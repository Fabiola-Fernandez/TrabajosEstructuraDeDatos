class Nodo {
    int dato;
    Nodo sig;
    Nodo(int d) { dato = d; }
}

class ListaCircular {
    Nodo cabeza;

    void insertar(int d) {
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

    void recorrer() {
        if (cabeza == null) return;

        Nodo temp = cabeza;
        do {
            System.out.print(temp.dato + " ");
            temp = temp.sig;
        } while (temp != cabeza);
    }
}

public class Main {
    public static void main(String[] args) {
        ListaCircular lista = new ListaCircular();
        lista.insertar(1);
        lista.insertar(2);
        lista.insertar(3);

        lista.recorrer();
    }
}
