class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)

n1.sig = n2
n2.sig = n3
n3.sig = n1  # circular

temp = n1
for i in range(6):
    print(temp.dato)
    temp = temp.sig
