def inver(lista):
    ocurrencias = ""
    if type(lista) == list:
        for x in lista:
            if type(x) == str:
                ocurrencias += x[::-1] +" "
        return ocurrencias
