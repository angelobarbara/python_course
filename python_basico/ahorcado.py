import random


images = ['''


    +---+
    |   |
        |
        |
        |
        |
        ========''','''


    +---+
    |   |
    O   |
        |
        |
        |
        ========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
        ========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        ========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ========''','''


    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ========''','''

    ''']

words = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado',
    'bocina',
    'automovil',
    'escenografia'
    ]

# def random_word():
#     idx = random.randint(0, len(words) - 1)
#     return words[idx]


def display_board(hidden_word,tries):
    print(images[tries])
    print()
    print(hidden_word)
    print('*---'*len(hidden_word), end = '*')
    print()

def run():
    word = words[random.randint(0, len(words) - 1)]
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = list()
        for i in range(len(word)):
            if word[i] == current_letter:
               letter_indexes.append(i) 

        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word,tries)
                print()
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter
            letter_indexes = list()

        try:
            hidden_word.index('-')
        except ValueError:
            print('¡Felicidades! Ganaste. La palabra era: {}'.format(word))
            break



    
if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()