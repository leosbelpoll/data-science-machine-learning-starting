# tambien llamamos: adivina y verifica

goal = int(input('Ingrese un entero: '))
result = 0

while result ** 2 < goal:
    result += 1

if result ** 2 == goal:
    print(f'La raiz exacta es: {result}')
else:
    print(f'El número {goal} no tiene raiz exacta')
