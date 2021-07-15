"""Definir una funcion que tome dos listas y devuelva True
si tiene al menos 1 miembro en comun o devuelva False
de lo contrario. Escribir la funcion usando el bucle for anidado"""








def superposicion(lista1,lista2):
    coincidencia = 0
    if type(lista1) == list and type(lista2) == list:
        for x in lista1:
            for j in lista2:
                if x == j:
                    coincidencia +=1
        if coincidencia > 0:
            return True
        else:
            return False
