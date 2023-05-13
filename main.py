from fastapi import FastAPI
import  pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app =FastAPI(
    
    title="Lista de scores de peliculas",
    description="El proyecto cuenta con un dataset de la industria cinematográfica que incluye películas producidas desde 1874 hasta el 2020. Este dataset provee información relevante como fechas de lanzamiento, presupuestos, recaudaciones, duración, puntuación, productoras y mucho más. Con esta valiosa información, se pueden llevar a cabo análisis y exploraciones de datos para descubrir tendencias y patrones en la industria del cine.",
    version="0.0.1"
)

df_movies = pd.read_csv("movies_dataset transformado.csv", sep=",", low_memory=False)

#Probando el servidor en root "/"
@app.get("/")
def index():
    return "Inicialización exitosa de la API"

#Función 1 - Peliculas por mes
@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron 
    ese mes historicamente'''
    mes = mes.title()
    cantidad = len(df_movies.loc[df_movies['month'] == mes, 'title'])
    return {'mes':mes, 'cantidad':cantidad}


#Función 2 - Peliculas por Día
@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron 
    ese dia historicamente'''
    dia = dia.title()
    cantidad = len(df_movies.loc[df_movies['day'] == dia, 'title'])
    return {'dia':dia, 'cantidad':cantidad}

#Funcion 3 cantidad y ganancia por franquicia
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    franquicia = franquicia.title()
    cantidad = len(df_movies.loc[df_movies["belongs_to_collection"] == franquicia])
    ganancia = df_movies["revenue"].loc[df_movies["belongs_to_collection"] == franquicia].sum()
    if cantidad == 0:
        return 'Información inexistente'
    else:
        ganancia_promedio = ganancia/cantidad
        return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia, 'ganancia_promedio':ganancia_promedio}

# Funcion 4 - peliculas por pais
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' 
    pais = pais.title()
    cantidad = 0
    lista = df_movies["production_countries"]
    for i in range(len(lista)):
        if lista[i] is None:
            continue
        if type(lista[i]) is not list and lista[i] == pais:
            cantidad += 1
        if pais in lista[i]:
            cantidad += 1
    return {'pais':pais, 'cantidad':cantidad}


# Funcion 5 - cantidad, ganancia por productoras
@app.get('/productoras/{productora}')
# Funcion 5 - cantidad, ganancia por productoras
def productoras(productora): 
    '''Ingresas la productora, retornando la ganancia toal y la cantidad de peliculas que produjeron'''
    productora = productora.title()
    ganancia_total = 0
    cantidad = 0
    lista = df_movies["production_companies"]
    for i in range(len(lista)):
        if lista[i] is None:
            continue
        if type(lista[i]) is not list and lista[i] == productora:
            cantidad += 1
            ganancia = df_movies["revenue"][i]
            ganancia_total += ganancia
        if productora in lista[i]:
            cantidad += 1
            ganancia = df_movies["revenue"][i]
            ganancia_total += ganancia
    
        return {'productora':productora, 
            'ganancia_total':ganancia_total, 
            'cantidad':cantidad}

productoras("Pixar Animation Studios")

#Funcion 6 - inversion, ganancia, retorno, año por pelicula
@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
    "ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en que se lanzo"
    pelicula_df = df_movies.loc[df_movies["title"] == pelicula.title()] 
    inversion = pelicula_df["budget"].iloc[0].item()
    ganancia = pelicula_df["revenue"].iloc[0].item()
    retorno = pelicula_df["return"].iloc[0].item()
    año = pelicula_df["release_year"].iloc[0].item()
    
    return {'pelicula':pelicula, 
            'inversion':inversion, 
            'ganacia':ganancia,
            'retorno':retorno, 
            'anio':año}


#Funcion 7 - Sistema de recomendacion
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''

    titulo = titulo.title()
    # Eliminar valores nulos en el DataFrame
    df_movies.dropna(subset=['title'], inplace=True)

    # Crear vectorizador TF-IDF
    vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=5, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df_movies['title'])

    # Crear matriz de similitud dispersa
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix, dense_output=False)
    # Obtener índice de película correspondiente al título
    idx = df_movies[df_movies['title'] == titulo].index[0]
    
    # Obtener puntajes de similitud de película correspondiente al índice
    sim_scores = list(enumerate(cosine_sim[idx].toarray().ravel()))
    
    # Ordenar películas por puntaje de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Obtener índices de las 5 películas más similares
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    
    # Devolver lista de los 5 títulos de películas más similares
    return df_movies['title'].iloc[movie_indices].tolist()