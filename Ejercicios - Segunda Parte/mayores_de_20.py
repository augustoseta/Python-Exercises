"""Definir una tupla con 10 edades  de personas.
Imprimr la cantidad de personas con edades superiores a 20.
Variar el ejercicio para que sea el usuario quien ingresa las edades"""





def mayor_de_20(tupla):
    mayores = 0
    if type(tupla) == tuple and len(tupla) == 10:
        for x in tupla:
            if x > 20:
                mayores +=1
	print("Cantidad de persones mayores de 20: ", mayores)





    #--------------------------------------------------------------------------#


def mayores_de_20():
    mayores = 0
    for x in range(10):
        edad = int(input("Ingrese edad: "))
        if edad > 20:
            mayores +=1
	print("Cantidad de mayores de 20: ", mayores)






