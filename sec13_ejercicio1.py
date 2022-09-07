'''
Crear una funcion "buscar" que mediante una expresion regular indique si una palabra esta en una frase
Probar la función "buscar" con estas frases:
    texto = "Esto es una frase de pruebas para hacer busquedas"
    palabra_a_buscar = "frase"
En caso de encontrar la palabra en la frase, indicar en que posición empieza y en cual finaliza.
'''

#importa modulo expresiones regulares
import re 

# define variables
texto = palabra_a_buscar = ""
busqueda = None



texto = "Esto es una frase de pruebas para hacer busquedas"

palabra_a_buscar = "frase"

#procesos
# crea la funcion para buscar la palabra en el texto
def buscar(pal, txt):
    resultado = re.search(pal, txt)
    return resultado

busqueda = buscar(palabra_a_buscar, texto)


# muestra resultados
if busqueda:
    posicion_ini = busqueda.start()
    posicion_fin = busqueda.end()
    print('La palabra "{}" está en el texto.'.format(palabra_a_buscar))
    print("Empieza en la posición {} y finaliza en la posición {} del texto.".format(posicion_ini, posicion_fin))
else:
    print('La palabra "{}" no se encuentra en el texto.'.format(palabra_a_buscar))

