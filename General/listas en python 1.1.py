lista=["jose","kevin","maria","alberto"]    #instruccion para crear una lista
lista.append("pacheco")                     #agregar otra variable a la lista

lista[4]="nicol"  #Para agregar o modificar un nombre de la lista especifico

import subprocess

subprocess.call('espeak -ves "Hola '+ lista[0] + '"', shell=True)
subprocess.call('espeak -ves "Hola '+ lista[1] + '"', shell=True)
subprocess.call('espeak -ves "Hola '+ lista[2] + '"', shell=True)
subprocess.call('espeak -ves "Hola '+ lista[3] + '"', shell=True)
subprocess.call('espeak -ves "Hola '+ lista[4] + '"', shell=True)


