from Nodo_Simple import Nodo_Simple

class Lista_Matrices:
    
    def __init__(self) -> None:
        self.primero = None
        self.longitud = 0
    
    def leng(self):
        return self.longitud
    
    def vacia(self):
        return self.primero == None
    
    def agregar_principio(self, Matrices):
        if self.vacia():
            self.primero = Nodo_Simple(datos = Matrices)
            self.longitud += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo_Simple(datos = Matrices)
        self.longitud += 1
    
    def recorrer(self):
        actual = self.primero
        while actual != None:
            print('Id: ', actual.datos.id)
            actual = actual.siguiente