import random

def empieza():
    
    numero_random=random.randint(0,20)

    while True:
        numero = int(raw_input("introduce un numero: "))
        if numero == numero_random:
            print("Numero encontrado")
            return False
        elif numero < numero_random:
            print("introduce un numero mas grande")

        else:
            print("introduce un numero mas pequeño")

if __name__ == '__main__':
    empieza()
    raw_input("presione enter para terminar")
