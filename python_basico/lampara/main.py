#import lamp
from lamp import Lamp

def run():
    #lamp = lamp.Lamp()
    lamp = Lamp(is_turned_on = True)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [e]ncender
            [a]pagar
            [s]alir
        '''))

        if command == 'e':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()