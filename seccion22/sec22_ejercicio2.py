'''
Crear 2 arrays con 9 números aleatorios enteros entre los valores 0 y 100
Cambiar el formato de los arrays en una estructura de 3 filas por 3 columnas
Crear 2 dataframes con esos arrays
concatenar esos 2 dataframes
'''

import pandas as pd
import numpy as np

# CREA ARRAYS CON VALORES ALEATORIOS CON LA FORMA 3X3
array1 = np.random.randint(0, 100, 9).reshape(3,3)
array2 = np.random.randint(0, 100, 9).reshape(3,3)

# CREA DATAFRAMES CON LOS VALORES DE LOS ARRAYS
dataframe1 = pd.DataFrame(array1)
dataframe2 = pd.DataFrame(array2)

# CONCATENA LOS DATAFRAMES 1 Y 2
dataframe3 = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframe3)