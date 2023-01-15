def promedio(temperatura):
    inicio = 0
    
    for temp in temperatura:
        if temp == 64:
            break
        inicio += float(temp)
    return inicio/len(temperatura)

if __name__ == '__main__':

    temperatura = [12,12,12,12,12,64,4]
    prom = promedio(temperatura)

    print("La temperatura primedio es {}".format(prom))
