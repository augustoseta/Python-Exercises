"""Definir una lista con un conjunto de nombres, imprimir la cantidad que empiezan
con la letra a.
Hacer otro programa que permita elegir al usuario la letra de inicio"""




def buscar_por_letra(lista):
    contador = 0
    if type(lista) == list:
        for x in lista:
            if type(x) == str:
                if x[0].lower() == 'a':
                    contador += 1
    print("Cantidad de nombres que empiezan con 'a' : ", contador)

#----------------------------------------------------------------------#

def buscar_por_eleccion(lista):
    contador = 0
    inicial = input("Ingrese letra inicial: ")
    if type(lista) == list and len(inicial) == 1:
        for x in lista:
            if type(x) == str:
                if x[0].lower() == inicial.lower():
                    contador +=1
    print("Cantidad de nombres con inicial ",inicial," : ",contador)

