'''
Leer el fichero adjunto "poblacion.xlsx" y cargar los datos en un dataframe
Con esos datos, visualizar cual es la ciudad más poblada en América
Leer el fichero adjunto "poblacion.csv" y cargar los datos en un dataframe
Con esos datos, visualizar cual es la ciudad más poblada de Africa
'''

# IMPORTA MODULOS NECESARIOS
import pandas as pd

# LEE EL FICHERO EXCEL
file_excel = pd.ExcelFile('C:/Users/Emanuel/Desktop/Cursos/Python/otros ejercicios/seccion21/poblacion.xlsx')


# CREA DATAFRAME CON LOS DATOS DE LA HOJA 1 DEL FICHERO EXCEL
df_excel = file_excel.parse('Hoja 1')

# CREA DATAFRAME CON LOS DATOS DE EL ARCHIVO CSV
file_csv = pd.read_csv('C:/Users/Emanuel/Desktop/Cursos/Python/otros ejercicios/seccion21/poblacion.csv')

# GUARDA LOS DATOS DE LA CIUDAD MAS POBLADA DE AMERICA EN UNA VARIABLE
most_populated_city_america = df_excel['Ciudad más poblada'][3]

# GUARDA LOS DATOS DE LA CIUDAD MAS POBLADA DE AFRICA EN UNA VARIABLE
most_populated_city_africa = file_csv['Ciudad más poblada'][1]

# MUESTRA POR CONSOLA LAS CIUDADES MAS POBLADAS
print("La ciudad mas poblada de América:", most_populated_city_america)
print("La ciudad mas poblada de Africa:", most_populated_city_africa)