lista=["jose","kevin","maria","alberto"]    #instruccion para crear una lista
lista.append("pacheco")                     #agregar otra variable a la lista

lista[4]="nicol"  #Para agregar o modificar un nombre de la lista especifico

import subprocess

for lista_bucle in lista:       #Condicional para crear un bucle de una lista
    subprocess.call('espeak -ves "Hola '+ lista_bucle + '"', shell=True)


