"""Crear una funcion que reciba una palabra y cuente cuantas letras 'a' tiene,
cuantas letras e tiene y asi hastas completar todas las vocales"""


def contar_vocales(palabra):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    if type(palabra) == str:
        a += palabra.lower().count("a")
        e += palabra.lower().count("e")
        i += palabra.lower().count("i")
        o += palabra.lower().count("o")
        u += palabra.lower().count("u")
    print("cantidad de veces que se repite la letra 'a' : ",a)
    print("cantidad de veces que se repite la letra 'e' : ",e)
    print("cantidad de veces que se repite la letra 'i' : ",i)
    print("cantidad de veces que se repite la letra 'o' : ",o)
    print("cantidad de veces que se repite la letra 'u' : ",u)

#----------------------------------------------------------------------------------#

def input_contar_vocales():
    palabra = input("Ingrese una palabra: ")
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    if type(palabra) == str:
        a += palabra.lower().count("a")
        e += palabra.lower().count("e")
        i += palabra.lower().count("i")
        o += palabra.lower().count("o")
        u += palabra.lower().count("u")
    print("cantidad de veces que se repite la letra 'a' : ",a)
    print("cantidad de veces que se repite la letra 'e' : ",e)
    print("cantidad de veces que se repite la letra 'i' : ",i)
    print("cantidad de veces que se repite la letra 'o' : ",o)
    print("cantidad de veces que se repite la letra 'u' : ",u)

