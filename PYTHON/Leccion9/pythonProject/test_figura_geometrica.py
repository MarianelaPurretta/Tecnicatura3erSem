from Cuadrado import Cuadrado  #Importamos la class Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8,'Azul')
cuadrado1.alto = 7 #No acepta este valor por el método encapsulado que hicimos
#cuadrado1.ancho = 7
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')  #llamamos a traves del objeto al
#método calcular_area


# MRO: Method Resolution Order
#print(Cuadrado.mro()) # nos va a dar el órden en que se van a jecutar los métodos
#dependiendo de las jerarquías de clas ya definidas

print(cuadrado1)
print('Creación de objeto clase Rectángulo'.center(50, '_'))

rectangulo1 = Rectangulo(3,9, 'Verde')
rectangulo1.ancho = 8 #no toma esa reasignacion gracias al metodo en el set
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#figura1 = FiguraGeometrica() No permite instanciar, abstracta

print(Cuadrado.mro())

