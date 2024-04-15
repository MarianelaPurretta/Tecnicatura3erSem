class MiClase:
    #variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia): #la var instancia da distintos valores
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClas2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClas2.variable_instancia)
print(miClas2.variable_clase)