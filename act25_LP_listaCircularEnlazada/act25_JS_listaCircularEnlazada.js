class Nodo {
    constructor(dato) {
        this.dato = dato;
        this.sig = null;
    }
}

class ListaCircular {
    constructor() {
        this.cabeza = null;
    }

    insertar(d) {
        let nuevo = new Nodo(d);

        if (!this.cabeza) {
            this.cabeza = nuevo;
            nuevo.sig = this.cabeza;
        } else {
            let temp = this.cabeza;
            while (temp.sig !== this.cabeza)
                temp = temp.sig;

            temp.sig = nuevo;
            nuevo.sig = this.cabeza;
        }
    }

    recorrer() {
        if (!this.cabeza) return;

        let temp = this.cabeza;
        do {
            console.log(temp.dato);
            temp = temp.sig;
        } while (temp !== this.cabeza);
    }
}

let lista = new ListaCircular();
lista.insertar(1);
lista.insertar(2);
lista.insertar(3);

lista.recorrer();
