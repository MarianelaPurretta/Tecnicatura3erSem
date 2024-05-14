


class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self): #Creamos el metodo y encapsulamos el codigo dentro
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf-8')
        return self.nombre

    def __exit__(self, tipo_exception, valor_exception, traza_error): #Trae parametros por default
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close() #Cerramos el archivo
