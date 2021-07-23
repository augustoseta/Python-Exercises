#Ejercicio de Herencia Multiple


class Telefono(object):
    def __init__(self):
        pass

    def llamar(self):
        print("llamando...")

    def ocupado(self):
        print('ocupado...')

class Camara(object):
    def __init__(self):
        pass


    def fotografia(self):
        print('tomando fotos...')

class Reproduccion(object):
    def __init__(self):
        pass

    def reproduccion_musica(self):
        print('reproducir musica...')

    def reproduccion_video(self):
        print('reproducir un video...')

class smarthphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print('telefono apagado')


#movil = smarthphone()
#print(movil.fotografia())


