#Importamos librerias necesarias para el proceso de ETL

import pandas as pd
import numpy as np
import json
import ast
import locale

#Cargamos la data 

datos = pd.read_csv("movies_dataset.csv", sep=",")

#Eliminamos duplicados existentes y reindexamos para evitar conflictos futuros

datos = datos.drop_duplicates(keep='first')
datos.reset_index(inplace=True, drop=True)

#Generamos 3 funciones para extraer información de las columnas anidadas de tipo Json

def convertir1(object):  
    Lista = []
    for i in ast.literal_eval(object):
        Lista.append(i['name'])
    return Lista

def convertir2(obj): 
    
    if isinstance(obj, str) and '{' in obj:
        dic = ast.literal_eval(obj)

        return dic['name']
    
def convertir3(obj): 
    if isinstance(obj, str) and '{' in obj:
        L=[]
        for i in ast.literal_eval(obj):
            L.append(i['name']);
        return L
    
#Aplicamos las funciones para desanidar las columnas tipo Json

datos["genres"]=datos["genres"].apply(convertir1)
datos['belongs_to_collection'] = datos['belongs_to_collection'].apply(convertir2)
datos['production_companies'] = datos['production_companies'].apply(convertir3)
datos['production_countries'] = datos['production_countries'].apply(convertir3)
datos['spoken_languages'] = datos['spoken_languages'].apply(convertir3)

print("columnas tipo Json desanidadas")

#reemplazamos los valores "0" por 0 de la columna "budget" y convertimos todo a dato numerico

datos["budget"] = datos["budget"].replace("0", 0)
datos['budget'] = pd.to_numeric(datos['budget'], errors='coerce')
print("columna budget corregida")

#reemplazamos por 0 valores nulos de la columna "revenue" y dejamos en formato numerico

datos["revenue"] = datos["revenue"].fillna(0)
datos["revenue"] = pd.to_numeric(datos["revenue"], errors='coerce')
print("columna revenue corregida")

#Transformación de fechas y creación de la columna "release_year"

datos['release_date'] = pd.to_datetime(datos['release_date'], format='%Y-%m-%d', errors='coerce')
datos["release_year"] = datos['release_date'].dt.year
datos['release_year'] = datos['release_year'].fillna(0).astype(int)
print("columna release_year creada")

#Creación de la columna "return" reemplazando nulos por ceros

def calculate_return(row):
    if row["budget"] != 0:
        return row["revenue"] / row["budget"]
    else:
        return 0

datos["return"] = datos.apply(calculate_return, axis=1)
print("columna return creada")

#Creamos una nueva columna llamada "month" para consultas de la API
 
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
datos["month"] = datos['release_date'].dt.strftime('%B').apply(lambda x: x.title() if type(x) != float else x)
print("Columna month creada")

#Creamos una nueva columna llamada "day" para hacer consultas desde la API

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
datos["day"] = datos['release_date'].dt.strftime('%A').apply(lambda x: x.capitalize() if type(x) != float else x)
datos["day"] = datos["day"].replace("Miã©rcoles", "Miercoles")
datos["day"] = datos["day"].replace("Sã¡bado", "Sabado")

print("columna day creada")

#Eliminacion de columnas que no se usaran: video,imdb_id,adult,original_title,vote_count,poster_path y homepage

datos.drop(columns=["video", "imdb_id", "adult", "original_title", "vote_count", "poster_path", "homepage", "id", "overview", "release_date", "status", "tagline" ], inplace=True, axis=1 )
print("columnas que no se usaran eliminadas")

#Procesando Nulos

datos["belongs_to_collection"].fillna("Sin dato", inplace=True) #se reemplazan nulos por "sin dato" 90%(40962)
datos.dropna(subset=['budget'], inplace=True) #se eliminan 3 nulos
datos.dropna(subset=['original_language'], inplace=True)#se eliminan 11 nulos
datos.dropna(subset=['popularity'], inplace=True) #se eliminan 3 nulos
datos["production_companies"].fillna("Sin dato", inplace=True) #se reemplazan nulos por "Sin dato"
datos["production_countries"].fillna("Sin dato", inplace=True) #se reemplazan nulos por "Sin dato"
datos.dropna(subset=['runtime'], inplace=True)#se eliminaron 246
datos["spoken_languages"].fillna("Sin dato", inplace=True)#se reemplazan nulos por "Sin dato"


#Exportamos el dataframe "datos" transformado en CSV, para que se pueda usar en el EDA y la API

df_movies = pd.DataFrame(datos)
df_movies.to_csv('movies_dataset transformado.csv')
print("Dataset transformado exportado")


