"""Escribir una funcion que tome una lista de palabras y un entero n, y devuelva las palabras
que tengan mas de n caracteres"""

def filtrar_palabras(lista, n):
    if type(lista) == list and type(n) == int:
        for i in lista:
            if len(i) > n:
                print(i)



