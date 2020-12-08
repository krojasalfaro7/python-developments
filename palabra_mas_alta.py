# File name: palabra_mas_alta.py
# Author: Kevin Rojas
# email: krojas.alfaro7@gmail.com
# Python Version: 3.8
# Algorito que encuentra la palabra mas alta de un texto (MEJORAR: Hacer mas generico)

if __name__ == '__main__':
    texto = "hola ewwerdsasd como te encuentras "
    texto_list = texto.split()
    number_list = list(map(lambda x: len(x), texto_list))
    index = number_list.index(max(number_list))
    print(texto_list[index])
