def primo(numero):
    
    if numero < 2:
        return False

    elif numero == 2:
        return True

    elif numero > 2 and numero % 2 == 0:
        return False
    
    else:
        for i in range(3,numero):
            if numero % i == 0:
                return False
    return True

def run():
    numero=int(raw_input("introduce un numero: "))
    resultado = primo(numero)
    
    if resultado is True:
        print("{} es un numero primo".format(numero))
    else:
        print("{} no es primo".format(numero))

if __name__ == '__main__':
    run()
