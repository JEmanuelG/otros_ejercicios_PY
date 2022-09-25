'''
Crear una lista con los valores numéricos del 0 al 30
Crear otra lista con los primeros 10 valores de la lista inicial
Crear otra lista con los últimos 10 valores de la lista inicial
Crear un bucle que recorra esta ultima lista de valores finales
'''

import numpy as np

# CREA LISTA CON NP EN EL RANGO DE 0 A 30
list1 = np.arange(30)
print(list1)

# CREA LISTA CON LOS PRIMEROS 10 VALORES DE LA LISTA 1
list2 = list1[:10]
print(list2)

# CREA LISTA CON LOS ÚLTIMOS 10 VALORES
list3 = list1[-10:]
print(list3)

# ITERA SOBRE LA LISTA 3
for num in list3:
    print(num)