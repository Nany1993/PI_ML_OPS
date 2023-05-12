
# PROYECTO INDIVIDUAL N°1
## Machine Learning Operations (MLOps)

<img src="https://www.themachinelearners.com/wp-content/uploads/2020/12/Presentacion1.png" alt="MLOps" width="600"/>

<div style="text-align: justify;">
**En este README encontrarán toda la documentación, e instrucciones, para poder utilizar la API que se solicito desarrollar.**

**Contexto del proyecto**
*El proyecto cuenta con un dataset de la industria cinematográfica que incluye películas producidas desde 1874 hasta el 2020. Este dataset provee información relevante como fechas de lanzamiento, presupuestos, recaudaciones, duración, puntuación, productoras y mucho más. Con esta valiosa información, se pueden llevar a cabo análisis y exploraciones de datos para descubrir tendencias y patrones en la industria del cine.*

**Desafios enfrentados**
*El proceso de ETL puede ser una tarea desafiante, especialmente cuando se trata de archivos con estructuras complejas, como los JSON. En el caso particular de este dataset de la industria cinematográfica, uno de los desafíos más importantes fue el manejo de las columnas anidadas en formato JSON, que requerían una limpieza y un preprocesamiento cuidadoso. Además, la presencia de numerosos valores nulos y formatos de datos inadecuados también representaron desafíos adicionales que requirieron soluciones creativas.*

**Archivos que encontrarás en este repositorio**
* movies_dataset.csv --> Dataset original de la industria cinematografica
* movies_dataset transformado.csv --> Dataset con proceso de ETL
* requirements.txt --> Archivo con las librerias de python
* EDA.ipynb --> Notebook con el análisis exploratorio de los datos
* ETL.py --> Script de python con las funciones para realizar el ETL
* README --> Introducción del proyecto e Instrucciones de uso
* main.py --> El código de la API, con las consultas para los endpoints y funciones auxiliares

## Evaluación del cumplimiento de los objetivos

*Este proyecto se enfoca en el desarrollo de una API utilizando el framework FastAPI para comunicar y disponibilizar datos de la industria cinematografica. El objetivo principal es realizar transformaciones específicas en los datos y disponibilizarlos a través de endpoints accesibles.*

*De forma específica, se ha completado los siguientes objetivos:*

* [Proceso del ETL](ETL.py)
* [Análisis Exploratorio de los datos](EDA.ipynb)
* [Deployment](https://nany1993-pi-ml-ops.onrender.com/docs)
* [Video](url: )

## Requerimientos

* *Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos*.

* *Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0*.

* *Los valores nulos del campo release date deben eliminarse.*

* *De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.*

* *Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.*

* *Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.*


## Endpoints de la Api

*La API cuenta con los siguientes endpoints:*

1-  [Cantidad de peliculas estrenadas historicamente por mes](https://nany1993-pi-ml-ops.onrender.com/docs#/default/peliculas_mes_peliculas_mes__mes__get)

2-  [Cantidad de peliculas estrenadas historicamente por día](https://nany1993-pi-ml-ops.onrender.com/docs#/default/peliculas_dia_peliculas_dia__dia__get)

3-  [Cantidad de peliculas estrenadas por franquicia - con su ganancia](https://nany1993-pi-ml-ops.onrender.com/docs#/default/franquicia_franquicia__franquicia__get)

4-  [Cantidad de peliculas estrenadas por país](https://nany1993-pi-ml-ops.onrender.com/docs#/default/peliculas_pais_peliculas_pais__pais__get)

5-  [Cantidad de peliculas estrenadas y ganancia por productora](https://nany1993-pi-ml-ops.onrender.com/docs#/default/productoras_productoras__productora__get)

6-  [Retorno de la inversión, ganancia y año en que se lanzo una pelicula en especifico](https://nany1993-pi-ml-ops.onrender.com/docs#/default/retorno_retorno__pelicula__get)

7-  [Sistema de recomendación de peliculas similares](https://nany1993-pi-ml-ops.onrender.com/docs#/default/recomendacion_recomendacion__titulo__get)

##Deployment

*Para realizar el deploy de esta aplicación se utilizo FASTAPI y RENDER.*



</div>"# PI-MLOPS_SOY_HENRY" 
"# PI_ML_OPS" 
