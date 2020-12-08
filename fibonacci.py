# File name: fibonacci.py
# Author: Kevin Rojas
# email: krojas.alfaro7@gmail.com
# Python Version: 3.8
# Algoritmo que calcula la serie de fibonacci de N numeros, apartir de 0.

if (__name__ == '__main__'):

    num = int(input()) #Entrada del usuario

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    for i in range(num):
        print(fibonacci(i)) #Llamada de la funcion