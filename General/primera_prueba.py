mensaje=input("\nInserte frase:\n")

import subprocess
subprocess.call('espeak -ves "hola"',shell=True)
