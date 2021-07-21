class Calculadora(object):
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multi = n1 * n2
        self.div = n1 / n2

operacion = Calculadora(7,8)
print(operacion.suma)