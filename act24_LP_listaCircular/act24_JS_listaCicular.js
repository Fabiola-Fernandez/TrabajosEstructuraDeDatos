class Nodo {
    constructor(dato) {
        this.dato = dato;
        this.sig = null;
    }
}

let n1 = new Nodo(1);
let n2 = new Nodo(2);
let n3 = new Nodo(3);

n1.sig = n2;
n2.sig = n3;
n3.sig = n1; // circular

let temp = n1;
for (let i = 0; i < 6; i++) {
    console.log(temp.dato);
    temp = temp.sig;
}
