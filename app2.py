# Importamos las bibliotecas necesarias
import requests
import json
import os
from dotenv import load_dotenv

# Variables de entorno desde el archivo dotenv.env
load_dotenv(dotenv_path="dotenv.env")


# URL
url_base="https://api.themoviedb.org/3/"
# Variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["api_key"]
# Código del país
code='EN'
# Diccionario que guarde nuestros parámetros
payload = {'api_key':key,"languaje":'en-EN'}
#Pedimos el título de una película por teclado y nos muestra el json de TheMovieDB
pelicula = input("Introduce el nombre de la pelicula: ")
# URL con los parámetros
url = url_base+'search/movie'+'?query='+pelicula
r=requests.get(url,params=payload)
#Guardamos en una variable el contenido de la respuesta
if r.status_code == 200:
    doc=r.json()
    #Mostramos el contenido de la respuesta
    print(json.dumps(doc, indent=4, sort_keys=True))
else:
    print ("Error")
    print (r.status_code)
