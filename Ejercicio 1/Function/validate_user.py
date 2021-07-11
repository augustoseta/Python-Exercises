def validate_user(username):
    if username.isalnum() != True:
        print("El nombre de usuario puede contener solo letras y numeros")
    elif len(username) < 6:
        print("El nombre de usuario debe contener al menos\n6 caracteres")
    elif len(username) > 12:
        print("El nombre de usuario no puede contener\nmas de 12 caracteres")
    else:
        return True
            
