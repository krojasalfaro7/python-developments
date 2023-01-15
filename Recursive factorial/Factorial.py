def getFactorial(numero):
    if(numero > 0):
        return numero*getFactorial(numero - 1)
    else:
        return 1

if __name__ == '__main__':
    x = 5
    print("El factorial de "+str(x)+" es = "+str(getFactorial(x)))
