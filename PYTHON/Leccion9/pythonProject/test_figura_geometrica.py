from Cuadrado import Cuadrado  #Importamos la class Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5,'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')  #llamamos a traves del objeto al
#método calcular_area


# MRO: Method Resolution Order
print(Cuadrado.mro()) # nos va a dar el órden en que se van a jecutar los métodos
#dependiendo de las jerarquías de clas ya definidas

print(cuadrado1)

rectangulo1 = Rectangulo(3,8, 'Verde')
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)