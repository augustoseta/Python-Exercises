def password_validation(password):
    upper_count = 0
    lower_count = 0
    num_count = 0
    special_count = 0
    if len(password) < 8:
        print("La contraseña no es segura")
    else:
        for x in password:
            if x == " ":
                print("La contraseña no puede contener espacios en blanco")
                break
            elif x.isupper() == True:
                upper_count += 1

            elif x.islower() == True:
                lower_count += 1

            elif x.isdigit() == True:
                num_count += 1

            elif x.isalnum() == False:
                special_count += 1

    if upper_count != 0 and lower_count !=0 and num_count!=0 and special_count != 0:
        return True
    else:
        print("Contraseña incorrecta")
