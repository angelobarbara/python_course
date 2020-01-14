for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i ** 2)

for i in range(30):
    if i % 3 == 0:
        print(i ** 2)
    elif i == 22:
        break

my_string = 'abcdefghi'
for letter in my_string:
    print(letter)