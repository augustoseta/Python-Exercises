##maximo de tres numeros

def max_of_three(x,y,z):
    if x > y and x>z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
