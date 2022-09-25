'''
Crear la funcion "pares" que devuelva un array de números pares
entre dos valores pasados como parámetros a la función (inicio y fin)
Utilizar la funcion "pares" con los numeros 1 y 30
Utilizar la funcion "pares" con los numeros 2 y 40
'''
# IMPORTA MODULO NUMPY
import numpy as np


# DEFINE FUNCION PARA GENERAR ARRAY CON NUM PARES
def pares(desde, hasta):
    ''' Esta funcion sirve para crear un arreglo con los números pares de un rango dado por paremetro (desde, hasta) '''
    # Asigna los valores de los parametros a variables internas
    # Se le suma 1 a fin para incluir el ultimo valor al rango
    inicio, fin = desde, hasta+1
    # CONTROLA QUE EL INICIO SEA NÚMERO PAR, DE LO CONTRARIO LE SUMA 1 PARA CONVERTIRLO EN NUMERO PAR
    if (inicio % 2) != 0:
        inicio += 1
    # CREA ARREGLO DE 2 EN 2
    array_p = np.arange(inicio, fin, 2)

    return array_p

# EJECUTA FUNCION CON VALORES 1 Y 30
array_pares = pares(1, 30)
print(array_pares)

# EJECUTA FUNCION CON VALORES 2 Y 40
array_pares = pares(2, 40)
print(array_pares)