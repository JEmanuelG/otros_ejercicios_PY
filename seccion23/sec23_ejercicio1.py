'''
Crear una lista de 1000 valores aleatorios que sigan una distribución normal
Crear un histograma mediante matplotlib con la lista de valores
Crear un diagrama de caja(donde se acumula el 50% de los valores) mediante seaborn
'''
import numpy as np
import matplotlib as mpl
import seaborn as sns

# CREA LISTA DE VALORES ALEATORIOS
list_valores = np.random.randn(1000)

# CREA GRAFICO DE HISTOGRAMA CON MATPLOTLIB
mpl.pyplot.hist(list_valores)
mpl.pyplot.show()

# CREA DIAGRAMA DE CAJA CON SEABORN
sns.boxplot(list_valores)
mpl.pyplot.show()