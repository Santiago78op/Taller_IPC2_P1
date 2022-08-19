from Paciente import Paciente
from Fila import Fila
from Matrice import Matriz
from Lista_Pacientes import Lista_Pacientes
from Lista_Doble_Filas import Lista_Doble_Filas
from Lista_Doble_Columnas import Lista_Doble_Columnas


columnas = Lista_Doble_Columnas()
columnas.insertar(1)
columnas.insertar(2)
columnas.insertar(3)

filas = Fila(1)
filas.lista_columnas.insertar(columnas)
matriz = Matriz(1)
matriz.lita_filas.insertar(filas)

paciente_1 = Paciente('Juan','23','10','6')
paciente_1.listaMatriz.agregar_principio(matriz)


matrices = Lista_Pacientes()

matrices.agregar_principio(paciente_1)


matrices.recorrer()