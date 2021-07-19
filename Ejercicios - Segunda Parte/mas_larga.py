""" Escribir una funcion que tome una lista de palabras y devuelva la mas larga """






def mas_larga(lista):
    while len(lista) > 0 and type(lista) == list:
        max_long = ""
        for x in lista:
            if type(x) == str:
                if len(x) > len(max_long):
                    max_long = x
        return max_long
