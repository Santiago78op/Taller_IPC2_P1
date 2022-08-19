from Nodo_Doble import Nodo_Doble

class Lista_Doble_Columnas:
    
    def __init__(self) -> None:
        self.primero = None
    
    def vacia(self):
        return self.primero == None
    
    def insertar(self, Columnas):
        if self.vacia():
            self.primero = Nodo_Doble(datos = Columnas)
        else:
            actual = Nodo_Doble(datos=Columnas , siguiente=self.primero)
            self.primero.anterior = actual
            self.primero = actual
    
    def recorrer(self):
        if self.vacia():
            return
        
        actual = self.primero
        print('Fila: ', actual.datos)
        
        while actual != None:
            actual = actual.siguiente
            print('Fila: ', actual.datos)