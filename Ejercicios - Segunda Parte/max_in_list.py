
"""Escribir una funcion que devuelva de una lista de numeros el mas grande"""



def max_in_list(lista):
    maximo = 0
    if type(lista) == list:
        for x in lista:
            if type(x) == int:
                if x > maximo:
                    maximo = x
                    return maximo
