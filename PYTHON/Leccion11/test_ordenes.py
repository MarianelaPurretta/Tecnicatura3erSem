from Orden import Orden
from Producto import Producto



producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Remera', 2000.00)
producto4 = Producto('Campera', 3500.00)
producto5 = Producto('Buzo', 5500.00)
producto6 = Producto('Zapatillas', 10500.00)
producto7 = Producto('Malla Hombre', 8000.00)
producto8 = Producto('Short', 6000.00)

productos1 = [producto1, producto2] #Creamos la lista de productos
orden1 = Orden(productos1)# Primer objeeto orden de lista productos
orden1.agregar_producto(producto5) #Agregamos productos
orden1.agregar_producto(producto3)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')

productos2 = [producto3, producto4, producto5]
orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')

productos3 = [producto5, producto6]
orden3 = Orden(productos3)
print(orden3)
print(f'Total de la orden3: {orden3.calcular_total()}')


productos4 = [producto7, producto8]
orden4 = Orden(productos4)
print(orden4)
print(f'Total de la orden4: {orden4.calcular_total()}')