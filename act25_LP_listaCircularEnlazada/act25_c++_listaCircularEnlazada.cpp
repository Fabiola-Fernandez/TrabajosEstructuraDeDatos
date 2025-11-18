#include <iostream>
using namespace std;

struct Nodo {
    int dato;
    Nodo* sig;
    Nodo(int d) : dato(d), sig(nullptr) {}
};

class ListaCircular {
private:
    Nodo* cabeza;

public:
    ListaCircular() : cabeza(nullptr) {}

    void insertar(int d) {
        Nodo* nuevo = new Nodo(d);

        if (!cabeza) {
            cabeza = nuevo;
            nuevo->sig = cabeza;
        } else {
            Nodo* temp = cabeza;
            while (temp->sig != cabeza)
                temp = temp->sig;
            temp->sig = nuevo;
            nuevo->sig = cabeza;
        }
    }

    void recorrer() {
        if (!cabeza) return;

        Nodo* temp = cabeza;
        do {
            cout << temp->dato << " ";
            temp = temp->sig;
        } while (temp != cabeza);
    }
};

int main() {
    ListaCircular lista;
    lista.insertar(1);
    lista.insertar(2);
    lista.insertar(3);

    lista.recorrer();
    return 0;
}
