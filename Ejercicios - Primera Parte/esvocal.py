#una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def is_vocal(caracter):
	vocals = "aeiou"
	while len(caracter) == 1:
		if caracter in vocals:
			return True
		else:
			return False
