from NumerosIgualesException import NumerosIgualesException

resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son números iguales') #raise permite largar una excepción

    resultado = a / b
except TypeError as e: #Clase hija de Exception
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e: #Clase hija de Exception
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e: #Exception:esta clase padre entonces es la mas genérica
    print(f'Exception - Ocurrió un error: {type(e)}')
#Bloque else, se ejecuta en caso que no encuentre ninguna excepcion
else:
    print("No se arrojó ninguna excepción")
#Bloque finalLy, siempre se ejecuta, se usa para liberar recursos
finally:
    print("Ejecución de este bloque finally")


print(f'El resultado es: {resultado}')
print('seguimos...')
