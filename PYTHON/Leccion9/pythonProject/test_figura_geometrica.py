from Cuadrado import Cuadrado  #Importamos la class Cuadrado

cuadrado1 = Cuadrado(5,'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')  #llamamos a traves del objeto al
#método calcular_area
print(cuadrado1.color)

# MRO: Method Resolution Order
print(Cuadrado.mro()) # nos va a dar el órden en que se van a jecutar los métodos
#dependiendo de las jerarquías de clas ya definidas

