
class Calculadora(object):
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_dato(self):
        self.datos = [int(input('Ingresar datos: ' + str(i+1) + '= ')) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b = self.datos
        s = a + b
        print(' el resultado es: ', s)

    def resta(self):
        a,b = self.datos
        r = a - b
        print(' el resultado es: ', r)

    def mult(self):
        a,b = self.datos
        m = a * b
        print(' el resultado es: ', m)

    def div(self):
        a,b = self.datos
        d = a / b
        print(' el resultado es: ', d)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def r_cuadrada(self):
        import math
        a, = self.datos
        print(' el resultado es: ', math.sqrt(a))





#objeto = op_basicas()
#print(issubclass(op_basicas,Calculadora))