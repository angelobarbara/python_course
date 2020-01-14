
def foreign_exchange_calculator(ammount):
    dolar_to_euro_rate = 0.90

    return dolar_to_euro_rate * ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte dolares a euros')
    print('')

    ammount = float(input('Introduzca la cantidad de dolares que quiere convertir: '))

    result = foreign_exchange_calculator(ammount)

    print('{} dolares son {} euros'.format(ammount,result))

if __name__ == '__main__':
    run()