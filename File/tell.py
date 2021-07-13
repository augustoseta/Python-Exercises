archivo = open("C:/Users/Beto/Desktop/Python/documento.txt", "r")
contenido = archivo.readline()
mas = archivo.read(archivo.tell() * 2)
if archivo.tell() > 50:
    archivo.seek(50)
