def primo(numero):
    
    if numero < 2:
        return False

    elif numero == 2:
        return True

    elif numero > 2:
        for i in range(3,numero):
            if numero%2==0:
                return False
            elif numero%i==0:
                return False
    else:
        return True


if __name__ == '__main__':  #indicacion para que python inicie el programa a partir de aqui

    while True:             #El while True lo use para que se repitiera la funcion constantemente
        numero=int(raw_input("introduce un numero: "))
        primo(numero)
        resultado = primo(numero)    #Tambien se puede asignar el valor de una funcion  una variable, es decir se podia colocar 'resultado = primo(numero)' en vez de llamar primero a la funcion
        if resultado is True:
            print("{} es un numero primo".format(numero))
        else:
            print("{} no es primo".format(numero))
