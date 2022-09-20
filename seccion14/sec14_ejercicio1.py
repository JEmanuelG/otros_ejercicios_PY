'''
- Crear una base de datos.

- Crear una tabla "productos" con 3 campos.
    id: Identificador del producto de tipo numérico
    nombre: Nombre del producto de tipo texto
    precio: precio del producto de tipo numerico

- Insertar 3 productos en la tabla "productos".
    1, "Impresora", 300
    2, "Mouse", 20
    3, "Computadora", 600

- Consultar los productos de la tabla "productos"

- Cerrar la base de datos.
'''
import sqlite3

# DEFINE VARIABLES
list_productos = list_productos_recuperados = []
conexion = cursor = None

list_productos = [
    (1, "Impresora", 300),
    (2, "Mouse", 20),
    (3, "Computadora", 600)
]

# CREA BASE DE DATOS
conexion = sqlite3.connect("datos_productos.db")

cursor = conexion.cursor()

# CREA TABLA PRODUCTOS
cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE TEXT, PRECIO INTEGER)")
conexion.commit()

#AGREGA DATOS A LA TABLA
cursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?)", list_productos)
conexion.commit()

# CONSULTA DATOS DE LA BASE DE DATOS
cursor.execute("SELECT * FROM PRODUCTOS")

# GUARDA DATOS OBTENIDOS
list_productos_recuperados = cursor.fetchall()

# MUESTRA DATOS EN CONSOLA
for producto in list_productos_recuperados:
    print(producto)


conexion.close()
