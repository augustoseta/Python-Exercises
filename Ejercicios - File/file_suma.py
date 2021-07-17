def leerNumero():
    archivo = open("numeros.txt" , "r")
    suma = 0
    contador = 0
    linea = archivo.readline()
    while linea:
        suma += int(linea)
        contador += 1
        linea= archivo.readline()
    print("suma :", suma)
    promedio = suma/contador
    print("promedio :", promedio)
    archivo.close()
    

leerNumero()
input()
