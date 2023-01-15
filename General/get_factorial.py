# File name: get_factorial.py
# Author: Kevin Rojas
# email: krojas.alfaro7@gmail.com
# Python Version: 3.8
# Funcion que calcula el factorial de un numero entero


def get_factorial(numero):
    if numero > 0:
        return numero*get_factorial(numero - 1)
    else:
        return 1


if __name__ == '__main__':
    x = 5
    print("El factorial de "+str(x)+" es = "+str(get_factorial(x)))
