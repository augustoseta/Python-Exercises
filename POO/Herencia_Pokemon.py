class Pokemon(object):
    def __init__(self, nombre, tipo):
        self.nombre = nombre      #mote del pokemon
        self.tipo = tipo

    def descripcion(self):
        return '{} ES UN POKEMON DE TIPO {}'.format(self.nombre, self.tipo)

class Charmander(Pokemon):
    def ataque(self, tipoataque):
        return '{} ejecuta un tipo de ataque: {}'.format(self.nombre, tipoataque)

class Bulbasaur(Pokemon):
    def ataque(self, tipoataque):
        return '{} ejecuta un tipo de ataque: {}'.format(self.nombre, tipoataque)



#nuevo_pokemon = Charmander('Charmie' , 'Fuego')
#print(nuevo_pokemon.descripcion())
#print(nuevo_pokemon.ataque(' LANZALLAMAS '))



