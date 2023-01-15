
def run():
    print('calculadora de divisas')
    
    cantidad = float(raw_input('ingresa la cantidad peso mexicanos a convertir'))
    
    foreign_exchange_calculator(cantidad)

    resultado = foreign_exchange_calculator(cantidad)
    print ('${} mexicano son ${} colombianos'.format(cantidad, resultado))
    

def foreign_exchange_calculator(cantidad):
    mex_to_col_rate = 145.97
    
    return mex_to_col_rate*cantidad


if __name__ == '__main__':
    run()
