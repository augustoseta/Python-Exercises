#Definir una funcion que reconoce palindromos (palabras que tienen el mismo aspecto escritas invertidas)
#ejemplo: es_palindromor("radar") tendria que devolver True


def es_palindromo(cadena):
    if cadena == cadena[::-1]:
        return True
