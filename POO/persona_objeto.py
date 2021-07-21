class Persona(object):
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre, self.año)

    def comentario(self, frase):
        return '{} dice {} '.format(self.nombre, frase)


doctor = Persona("AUGUSTO" , 23)
print(doctor.descripcion())
print(doctor.comentario('Estoy practicando POO ;)'))
