class Nodo {
    int dato;
    Nodo sig;
    Nodo(int d) { dato = d; }
}

public class Main {
    public static void main(String[] args) {
        Nodo n1 = new Nodo(1);
        Nodo n2 = new Nodo(2);
        Nodo n3 = new Nodo(3);

        n1.sig = n2;
        n2.sig = n3;
        n3.sig = n1;  // circular

        Nodo temp = n1;
        for (int i = 0; i < 6; i++) {
            System.out.print(temp.dato + " ");
            temp = temp.sig;
        }
    }
}
