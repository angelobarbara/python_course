
def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = round((low + high) / 2)

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)

    else:
        return binary_search(numbers, number_to_find, mid + 1, high)
 
if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10,12,15,19,20,25,30,35,36,40,41,42,45,49,50,51]

    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número {} se encuentra en la lista.'.format(number_to_find))
    else:
        print('El número {} no se encuentra en la lista.'.format(number_to_find))
