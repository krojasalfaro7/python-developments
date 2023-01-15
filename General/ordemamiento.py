#ordenamiento

lista = [3,1,4,56,2,1,4,6]

print sorted(lista) #ordena de menor a mayor una lista
print sorted(lista,reverse=True)#ordena de manera inversa

lista.sort() #ordena la lista de mayor a menor y guarda el cambio
print lista

lista.sort(reverse=True) #ordena la lista de manera inversa y guarda el cambio
print lista

#ordenamiento con letra y numeros

letra = ['hola','a','A','inglish','live',5]

print letra

print sorted(letra)
print sorted(letra,reverse=True)

letra.sort()
print letra

letra.sort(reverse=True)
print letra
