class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other): #OTHER = OTRO
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

persona1= Persona("Ariel", 40)
persona2= Persona("Betancud", 5)

#persona1.__add__(persona2) Sintaxis interna

print(persona1 + persona2) # Sintaxis correcta
print(persona1 - persona2)