"""Realizar un programa que conste de una clase llamada Alumno
 que tenga como atributos el nombre y la nota del alumno.
 Definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje
 con el resultado de la nota y si ha aprobado o no"""

class Alumno:
    # Inicializamos los atributos
    def __init__(self, nombre, nota):
         self.nombre = nombre
         self.nota = nota

    def imprimir(self):
        print("Alumno: ", self.nombre)
        print("Nota: ", self.nota)
        print("")
    
    def resultado(self):
        if self.nota < 5:
            print("El alumno ha reprobado")
        else:
            print("El alumno ha aprobado")



alumno1 = Alumno("Lucas" , 4)
alumno2 = Alumno("Augusto" , 10)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()


