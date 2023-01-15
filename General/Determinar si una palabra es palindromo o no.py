def palindromo(word):
    invertir_palabra= word[::-1]
    if invertir_palabra == word:
        return True
    return False

if __name__ == '__main__':

    while True:
        
        word = str(raw_input("Introduce una palabra: "))
        resultado = palindromo(word)
        if resultado is True:
            print("{} es palindromo".format(word))
        else:
            print("{} no es palindromo.".format(word))
