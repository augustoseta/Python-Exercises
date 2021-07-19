def crearArchivo():
    archivo = open("agenda.txt" , "w")
    archivo.close()

def escribir():
    archivo = open("agenda.txt" , "a")
    print("Escribe un texto")
    cadena = input()
    archivo.write(cadena + "\n")
    archivo.close()

def leer():
    archivo = open("agenda.txt" , "r")
    linea = archivo.readline()
    while linea:
        print(linea)
        linea = archivo.readline()
    archivo.close()


"crearArchivo()"
"input()"


"escribir()"
"input()"

"leer()"
"input()"