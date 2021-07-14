archivo = open("C:/Users/Beto/Desktop/Python/documento.txt" , "r+")
contenido = archivo.read()
file_name = archivo.name
file_mode = archivo.mode
encoding = archivo.encoding
archivo.close()
if archivo.closed:
    print("El archivo se ha cerrado correctamente")
else:
    print("El archivo permanece abierto")

print(file_name)

print(file_mode)

print(encoding)
    
