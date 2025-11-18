#include <iostream>
using namespace std;

struct Nodo {
    int dato;
    Nodo* sig;
};

int main() {
    Nodo* n1 = new Nodo{1, nullptr};
    Nodo* n2 = new Nodo{2, nullptr};
    Nodo* n3 = new Nodo{3, nullptr};

    n1->sig = n2;
    n2->sig = n3;
    n3->sig = n1;   // Cierra el ciclo

    Nodo* temp = n1;
    for (int i = 0; i < 6; i++) { // recorre dos ciclos
        cout << temp->dato << " ";
        temp = temp->sig;
    }

    return 0;
}
