
def first_not_repeating_char(string_sequence):
    seen_letters = {}

    for idx, letter in enumerate(string_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key,value[0]))

    not_repited_letters = sorted(final_letters, key = lambda value: value[1])
    
    if not_repited_letters:
        return not_repited_letters[0][0]
    else:
        return '_'

if __name__ == '__main__':
    string_sequence = str(input('Introduzca una cadena de texto: '))
    result = first_not_repeating_char(string_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))