from Nodo_Doble import Nodo_Doble

class Lista_Doble_Filas:
    
    def __init__(self) -> None:
        self.primero = None
    
    def vacia(self):
        return self.primero == None
    
    def insertar(self, Filas):
        if self.vacia():
            self.primero = Nodo_Doble(datos = Filas)
        else:
            actual = Nodo_Doble(datos=Filas, siguiente=self.primero)
            self.primero.anterior = actual
            self.primero = actual
    
    def recorrer(self):
        if self.vacia():
            return
        
        actual = self.primero
        print('Fila: ', actual.datos.fila)
        
        while actual != None:
            actual = actual.siguiente
            print('Fila: ', actual.datos.fila)
            