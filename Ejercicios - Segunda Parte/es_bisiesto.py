def es_bisiesto():
    print("Ingrese un año y te dire si es bisiesto.")
    año = int(input("Año: "))
    if año % 4 == 0 and año % 100 != 0:
        print(año," es bisiesto porque es multiplo de 4")
    elif año % 400 == 0:
        print(año," es bisiesto porque es multiplo de 400")
    else:
        print(año, "no es bisiesto")


es_bisiesto()