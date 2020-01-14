pares = [x for x in range(100) if x % 2 == 0]
#pares = [x for x in range(2,100,2)]
impares = [x for x in range(100) if x % 2 != 0]
#impares = [x for x in range(1,100,2)]
cuadrados = {x: x**2 for x in range(100)}

print(pares)
print(impares)
print(cuadrados)