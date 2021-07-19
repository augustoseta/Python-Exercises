#suma los numeros dentro de una lista, si es un str lo ignora


def suma(lista):
	contador = 0
	while type(lista) == list:
		for x in lista:
			if type(x) == int or type(x) == float:
				contador +=x
		return contador
