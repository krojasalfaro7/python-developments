# Colocar una serie de números impares hasta el 100, que comience a partir del número colocado en pantalla

#import math

print 'Se colocora una serie de números impares hasta el 100 comenzando a partir del valor colocado a continuacion'

numero=input('coloca el valor de inicio: ')

while numero>=100:
    print ('el número debe ser menor escricto que 100')
    numero=input('coloca otra vez el valor de inicio: ')

if numero%2==0:
    numero=numero+1
    for x in range(numero,100,2):
        print x
else:
    for x in range(numero,100,2):
        print x
