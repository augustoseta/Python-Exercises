def leerVocales():
    archivo = open('texto.txt' , 'r')
    vocales = 'aeiou'
    contador = 0
    cadena = archivo.readline()
    while cadena:
        for vocal in cadena:
            if vocal in vocales:
                contador +=1
        cadena = archivo.readline()
    print("cantidad de vocales encontradas :", contador)
    archivo.close()
    


leerVocales()
input()
