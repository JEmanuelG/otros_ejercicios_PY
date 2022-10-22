'''
Crear un array con 100 números enteros aleatorios con valores entre 0 y 500
Utilizar un diagrama de caja para representar los valores aleatorios generados
'''
import numpy as np
import matplotlib as mpl
import seaborn as sns

# CREA LISTA DE VALORES ALEATORIOS
list_valores = np.random.randint(0, 500, 100)

# CREA DIAGRAMA DE CAJA CON SEABORN
sns.boxplot(list_valores)
mpl.pyplot.show()