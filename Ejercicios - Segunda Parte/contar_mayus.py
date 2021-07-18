"""Escribir un programa que le diga al usuario que ingrese uan cadena.
El programa tiene que evaluar la cadena y decir cuantas letras mayusculas tiene"""

def c_mayusculas(cadena):
    contador = 0
    if type(cadena) == str:
        for x in cadena:
            if x.isupper():
                contador +=1
    return contador
