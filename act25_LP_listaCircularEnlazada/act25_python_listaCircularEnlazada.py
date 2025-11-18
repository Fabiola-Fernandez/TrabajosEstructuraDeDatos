class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, d):
        nuevo = Nodo(d)

        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.sig = self.cabeza
        else:
            temp = self.cabeza
            while temp.sig != self.cabeza:
                temp = temp.sig

            temp.sig = nuevo
            nuevo.sig = self.cabeza

    def recorrer(self):
        if self.cabeza is None:
            return

        temp = self.cabeza
        while True:
            print(temp.dato)
            temp = temp.sig
            if temp == self.cabeza:
                break

lista = ListaCircular()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)

lista.recorrer()
