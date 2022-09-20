'''
A partir de la lista "numeros" que contiene números del 1 al 10,
Obtener mediante "filter" una lista denominada "pares" con los números pares de la lista "números"
'''

# Define funcion para determinar numeros pares

def pares(numeros):
    ''' Esta función sirve para determinar si un número dado por parametro es par.
        Retorna True si es par y False si no lo es.'''

    if (numeros % 2) == 0:
        return True
    else:
        return False
    

num_list = [1,2,3,4,5,6,7,8,9,10]

# Crea lista con numeros pares de la lista list_num por medi de filter
num_pares = list(filter(pares, num_list))

# Muestra lista creada
print(num_pares)