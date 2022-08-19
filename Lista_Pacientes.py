from Nodo_Simple import Nodo_Simple

class Lista_Pacientes:
    
    def __init__(self) -> None:
        self.primero = None
    
    def vacia(self):
        return self.primero == None
    
    def agregar_principio(self, Paciente):
        if self.vacia():
            self.primero = Nodo_Simple(datos = Paciente)
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo_Simple(datos = Paciente)
    
    def recorrer(self):
        actual = self.primero
        while actual != None:
            cantidad = actual.datos.listaMatriz.leng()
            print('Nombre: ', actual.datos.nombre,
                  'Edad: ', actual.datos.edad,
                  'Periodos: ', actual.datos.periodos,
                  'Cantidad de Matrices: ', cantidad)
            actual = actual.siguiente