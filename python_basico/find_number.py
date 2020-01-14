import random

def run():
    #number_found = False
    random_number = random.randint(0, 20)

    #while not number_found:
    while True:
        number = int(input('Introduzca un número: '))
        if number == random_number:
            print('Felicidades encontraste el número')
            #number_found = False
            return False
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    run()