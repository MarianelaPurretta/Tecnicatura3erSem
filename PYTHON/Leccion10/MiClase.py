class MiClase:
    #variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia): #la var instancia da distintos valores
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico(): #no recibe self porque no puede acceder ni al dinamico ni a los atributos
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls): #Recibimos el cls (recomendado pos python) porque es una referencia a la clase
        print(cls.variable_clase) #Accedemos a la var de clase

    #Método de instancia
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'Valor de variable clase 2' #Creamos la var y asignamos un valor
print(MiClase.variable_clase2) #Accedemos a los metodos de la Clase usando un objeto
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

#Llamamos al método
MiClase.metodo_estatico()

MiClase.metodo_clase() #Accedemos al los metodos de Clase usando la clase misma
#Creamos un objeto y con él el contexto dinámico
miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase() # Desde el contexto dinamico accedemos al estatico(clases)
miObjeto1.metodo_instancia()