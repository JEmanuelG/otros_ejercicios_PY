'''
Dado el fichero excel que adjunto en varios formatos
Copiar los datos al porta papeles
Crear un dataframe "datos" con esos datos copiados.
Mostrar por pantalla todos los datos del dataframe
Mostrar todos los nombres de columnas del dataframe
Mostrar la primera fila del dataframe
Mostrar todas las filas pero sólo las columnas "Continente" y "Población"
Mostrar las primeras 3 filas del dataframe
Mostrar las 2 últimas filas del dataframe
'''

# IMPORTA MODULOS NECESARIOS
import pandas as pd

# CREA DATAFRAME "datos"
datos = pd.read_clipboard()

# MUESTRA TODOS LOS DATOS DEL DATAFRAME
print(datos)

# MUESTRA LOS NOMBRES DE LAS COLUMNAS
print(datos.columns)

# MUESTRA LA PRIMERA FILA DEL DATAFRAME
print(datos.loc[0])

# MUESTRA LAS COLUMNAS REQUERIDAS Y SUS FILAS
print(datos[['Continente','Población']])

# MUESTRA LAS PRIMERAS 3 FILAS DEL DATAFRAME
print(datos.head(3))

# MUESTRA LAS ÚLTIMAS 2 FILAS DEL DATAFRAME
print(datos.tail(2))

