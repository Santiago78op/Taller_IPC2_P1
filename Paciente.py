from Lista_Matrices import Lista_Matrices


class Paciente:
    
    def __init__(self, nombre, edad, size, periodos) -> None:
        self.nombre = nombre
        self.edad = edad
        self.size = size
        self.periodos = periodos
        self.listaMatriz = Lista_Matrices()