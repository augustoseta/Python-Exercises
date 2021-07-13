archivo = open("documento.txt", "r+")
contenido = archivo.read()
final_del_archivo = archivo.tell()
lista = ['Linea 1\n', 'Linea 2\n']
archivo.writelines(lista)
archivo.seek(final_del_archivo)
print(archivo.readline())
print(archivo.readline())
