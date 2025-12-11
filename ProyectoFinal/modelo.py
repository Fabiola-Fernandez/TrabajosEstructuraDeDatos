import uuid
import json

class Nodo:
    def __init__(self, nombre, tipo, contenido=""):
        # Generamos un ID único random
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        # para el tipo de carpeta o archivo
        self.tipo = tipo
        # las carpetas vasias y los arhivos con el contenido
        self.contenido = contenido
        # lista de hijos
        self.hijos = []

    def agregar_hijo(self, nodo):
        """Método auxiliar para conectar nodos manualmente por ahora"""
        if self.tipo == 'carpeta':
            self.hijos.append(nodo)
        else:
            raise Exception("Un archivo no puede tener hijos")

    def to_dict(self):
        """
        Convierte el nodo y sus hijos
        Para el dia 4
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "contenido": self.contenido,
            "hijos": [hijo.to_dict() for hijo in self.hijos]
        }

    def __repr__(self):
        return f"<{self.tipo}: {self.nombre}>"