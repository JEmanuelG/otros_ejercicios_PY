'''
Obtener la tabla de paises de la pagina "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses"
Limpiar los datos lo necesario para que los nombres de las columnas sean correctos.
'''
# IMPOTA MODULOS NECESARIOS
import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'

# CREA DATA FRAME CON LOS DATOS DEL HTML
df_url = pd.io.html.read_html(url)
print(df_url)


# CREA DATA FRAME CON LA TABLA PRINCIPAL DE LOS PAISES
df_countries = df_url[0]
print(df_countries)