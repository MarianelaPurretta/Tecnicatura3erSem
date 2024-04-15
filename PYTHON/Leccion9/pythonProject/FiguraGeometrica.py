#CONVERTIMOS TODA L CLASE EN ABSTRACTA
from abc import ABC, abstractmethod
# ABC= Abstract Base Class,

#Primera Clase padre
class FiguraGeometrica(ABC): #aGRAGAMOS LA CLASE ABST.. (ABC)
    def __init__(self, ancho, alto): #Encapsulamos con_
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self.ancho = 0
            print(f'Valor erróneo para el ancho: {ancho}')
        if 0 < alto < 10:
            self._alto = alto
        else:
            self.alto = 0
            print(f'Valor erróneo para el alto: {alto}')
#CREAMOS LOS GETTER AND SETTER
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erróneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):#validaciones dentro de los set
            self._alto = alto
        else:
            print(f'Valor erróneo alto: {alto}')

    #AGREGAMOS EL MÉTODO ABSTRACTO: (sin implementar)
    @abstractmethod
    def calcular_area(self):
        pass


    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    #CREAMOS UN MÉTODO PARA VALIDAD VALORES:
    def _validar_valores(self, valor): #MÉTODO ENCAPSULADO
        return True if 0 < valor < 10 else False
