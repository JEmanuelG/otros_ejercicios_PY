'''
Vamos a filtrar datos en un dataframe.
Crearemos una lista de 50 valores aleatorios entre los valores 0 y 100
convertiremos esta lista en un dataframe para visualizar solo los valores que sean mayores de 50
'''
import numpy as np
import pandas as pd

# CREA UN ARREGLOS CON 50 VALORES ENTRE 0 Y 100
list_valores = np.random.randint(0, 100, 50)
print(list_valores)

# CAMBIA LA FORMA DEL ARRAY EN 5X10
list_valores.resize(5,10)

# CREA DATAFRAME CON LOS DATOS DEL ARRAY
dataframe = pd.DataFrame(list_valores)

# MUESTRA EN CONSOLA EL DATAFRAME SOLO CON LOS DATOS MAYORES A 50
print(dataframe[dataframe > 50])