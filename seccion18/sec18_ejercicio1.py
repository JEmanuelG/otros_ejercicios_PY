'''
Crear la funcion "primos" que será una función generadora de numeros primos entre 0 y 100
Esta es la lista de números primos entre 0 y 100:
numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
Utilizar la funcion generadora para mostrar por pantalla numeros primos menores de 50
'''

#Define funcion generadora

def primos(numero):
    numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    for n in range(numero):
        if (n in numeros_primos):
            yield n


maximo = 50

for num in primos(maximo):
    print(num)
