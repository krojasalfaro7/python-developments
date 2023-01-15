def factorial(numero):  #para la recursividad se debe establecer una condicion inicial
    if numero == 0:
        return 1

    return numero * factorial(numero - 1)

if __name__ == '__main__':

    while True:
        numero = int(raw_input("introduce un numero: "))
        resultado = factorial(numero)
        print ("factorial de {} es {}".format(numero,resultado))
