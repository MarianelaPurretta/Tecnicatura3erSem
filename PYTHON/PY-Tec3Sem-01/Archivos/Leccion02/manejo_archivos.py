# Para abrir un archivo primero declaramos una variable:
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #metodo "open" para abrir o crear archivos en caSo de que no exista
    # 'w': write ||| usamos encoding=utf8 para poder visualizar los acentos en el texto
    archivo.write('\nProgramamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Las letras son:\na: append  \nw: write  \nr: read  \nx: crear archivo especificado  \n')
    archivo.write('t: para texto o text, \nb: para binario o texto, \nw+: lee y escribe, \nr+: lee y escribe igual a w\n')
    archivo.write('Saludos a a todos\n')
    archivo.write('Con esto terminamos\n')
except Exception as e:
    print(e)
finally:
    archivo.close() # SIEMPRE SE DEBE CERRAR CON .CLOSE()

#archivo.write('Todo quedó perfecto') # Error: ya esta cerrado el archivo ya no podemos trabajar el el!
