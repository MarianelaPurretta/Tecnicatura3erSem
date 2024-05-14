from ManejoArchivos import ManejoArchivos
#Palabra -with-
#Manejo de contexto with: Abrimos el archivo modo lectura y renombramos la variable|Abre el arch y tb lo cierra
#Sin usar TRY ni FINALLY simplificamos codigo y abrimos y cerramos el archivo || sintaxis simplificada
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
    #print(archivo.read())
#EN ESTE CONTEXTO SE EJECUTA DE MANERA AUTOMATICA LOS METODOS:
#Usa distintos metodos: __enter__(donde se abre) y __exit__(donde se cierra)
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())