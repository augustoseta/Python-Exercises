#f-string

class Estudiante(object):
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #def __str__(self):
        #return f'hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años'

    def __repr__(self):
        return f'hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años'


nuevo_estudiante = Estudiante('augusto' , 'seta' , 23)
#print(f'{nuevo_estudiante}')
print(f'{nuevo_estudiante !r}')
