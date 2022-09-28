'''
Tenemos 3 clases "clase1", "clase2", "clase3"
Vamos a generar un número aleatorio de alumnos por clase
Crear una serie de clases y alumnos
Utilizar el indice de la serie creada para saber el número de alumnos de la clase 2
'''

# IMPORTA MODULOS NECESARIOS
import numpy as np
import pandas as pd

# CREA UNA LISTA DE 3 NUMEROS ALEATORIOS ENTRE 20 Y 50
list_students = np.random.randint(20,50,3)

# CREA UNA LISTA DE LAS CLASES PARA USAR COMO INDICE
list_class = ['clase1', 'clase2', 'clase3']

# CREA UNA SERIE CON LOS VALORES DE LIST_STUDENTS Y LIST_CLASS COMO INDICES
clasrooms = pd.Series(list_students, index=list_class)

# MUESTRA POR CONSOLA LA CANTIDAD DE ALUMNOS SEGUN INDICE REQUERIDO (CLASE2)
print(clasrooms['Clase2'])
