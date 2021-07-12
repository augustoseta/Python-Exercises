##función que calcule la longitud de una lista o una cadena dada sin utilizar len().

def long_list(parametro):
	long = 0
	for x in parametro:
		long +=1
	return long
