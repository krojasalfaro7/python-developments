# Colocar una serie de n�meros impares hasta el 100, que comience a partir del n�mero colocado en pantalla

#import math

print 'Se colocora una serie de n�meros impares hasta el 100 comenzando a partir del valor colocado a continuacion'

numero=input('coloca el valor de inicio: ')

while numero>=100:
    print ('el n�mero debe ser menor escricto que 100')
    numero=input('coloca otra vez el valor de inicio: ')

if numero%2==0:
    numero=numero+1
    for x in range(numero,100,2):
        print x
else:
    for x in range(numero,100,2):
        print x
