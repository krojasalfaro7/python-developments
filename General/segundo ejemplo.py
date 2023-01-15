def suma(num1,num2):        #Definiendo la variable suma y devulve el resultado 
    return num1 + num2      #devuelve el resultado con la suma de las variables

n1=int(raw_input("introduce el primer numero: "))
n2=int(raw_input("introduce el segundo numero: ")) #asignando la variable de tipo entero a n2 y n1

print ('el valor de la suma es:', suma(n1,n2)) #para python 3.2
print 'el valor de la suma es:', suma(n1,n2) #para python 2.6
raw_input()
