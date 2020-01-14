def palindrome2(word):
    return True if word[::-1] == word else False

def palindrome(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0,letter)
    reversed_word = ''.join(reversed_letters)
    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word = str(input('Escriba una palabra: '))
    result = palindrome(word.replace(' ',''))

    if result is True:
        print('{} es un palíndromo'.format(word))
    else:
        print('{} no es un palíndromo'.format(word))


    result = palindrome2(word.replace(' ',''))
    
    if result is True:
        print('{} es un palíndromo'.format(word))
    else:
        print('{} no es un palíndromo'.format(word))
