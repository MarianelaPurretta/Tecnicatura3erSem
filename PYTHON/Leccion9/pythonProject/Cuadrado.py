#Clase hija
#Importamos las clases padres
from Color import Color
from FiguraGeometrica import FiguraGeometrica
#Creamos clase Cuadrado hija de fig geom y color
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super.__init__(lado) #llamamos a la clase padre con super, pero con herencia múltiple no
        #sirve
        FiguraGeometrica.__init__(self, lado, lado) #Así llamamos la clase padre
        Color.__init__(self, color)#Inicializamos en clase padre color

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self): #Sobre escribimos el método __str__
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'