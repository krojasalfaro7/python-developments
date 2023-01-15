#Determinar que numero es mayor

print("Determinar cual de los 2 numeros a continuacion es mayor\n")
x1=raw_input("Introduce el primer número: ")

# mini prueba adicional, era para ver si funcionaba!!!
espacio=x1.count(" ")   #cuenta el numero de espacios introducidos y lo guarda en la variable espacio
print espacio
#fin del adicional

x2=raw_input("Introduce el otro número: ")

if (x1>x2):
    print x1,'es mayor que',x2
    raw_input("Presione enter para salir")
else:
    if (x1==x2):
        print ('Son iguales')
        raw_input("Presione enter para salir")
    else:
         print x2,'es mayor que',x1
         raw_input("Presione enter para salir")
