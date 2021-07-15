# multiplica todos los numeros dentro de una lista e ignora los str


def mult(lista):
	contador = 1
	while type(lista) == list:
		for x in lista:
			if type(x) == int or type(x) == float:
				contador *=x
		return contador
