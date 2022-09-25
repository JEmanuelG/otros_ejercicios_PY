'''
1. Crear una lista con números del 10 al 19
2. Crear otra lista con números del 50 al 59
3. Crear una matriz 2x10 con las listas anteriores
4. Crear otra matriz cuyos valores sean iguales a la matriz anterior multiplicados por 2
'''
# IMPORTA MODULO NUMPY
import numpy as np

list_1 = np.arange(20)
list_2 = np.arange(50,60)

# CREA MATRIZ CON LISTAS PREVIAMENTE CREADAS
matriz = np.array((list_1, list_2))
print(matriz)

# MULTIPLICA X 2 LA SEGUNDA MATRIZ
matriz_x2 = matriz * 2
print(matriz_x2)