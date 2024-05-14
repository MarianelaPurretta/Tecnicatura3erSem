# modo para leer:
# 1 read :'r'

archivo = open('prueba.txt', 'r', encoding='utf8') #en los () especificamos la ruta del archivo: C:\\
# print(archivo.read())
# print(archivo.read(16)) #Muestra las primeras(n)letras del texto
# print(archivo.readline())
# print(archivo.readline())

# Iteramos el archivo:
# for linea in archivo:
    # print(linea)
# Metodo que muestra una lista

# ANEXAMOS INFORMACION, COPIAMOS A OTRO:

archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()

print('Se ha terminado el proceso de leer y copiar archivos')