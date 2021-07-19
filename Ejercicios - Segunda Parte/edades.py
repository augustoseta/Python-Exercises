"""Escribir un programa donde:
    - Se ingresa el año en curso
    - Se ingresa el nombre y el año de nacimiento de tres personas
    - Se calcula cuantos años cumpliran durante el año en curso
    - Se imprime en pantalla"""


def main():
    año = int(input("Ingrese año en curso: "))
    for x in range(3):
        nombre = input("Ingrese nombre de la persona: ")
        nacimiento = int(input("Ingrese año de nacimiento: "))
        edad = año - nacimiento
        print(nombre, " cumplira este año ",edad, " años")

main()