"""Definir un histograma que tome una lista de numeros enteros e imprima
un histograma en la pantalla. Ejemplo: procedimiento([4,9,7]) deberia imprimir:

****
*********
*******

"""



def procedimiento(lista):
    if type(lista) == list:
        for x in lista:
            if type(x) == int:
                print("*" * x)
