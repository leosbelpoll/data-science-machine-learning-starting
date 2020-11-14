# Similar a enumeración exhaustiva, pero no necesita una respuesta exacta.
# Podemos aproximar soluciones con un margen de error que llamaremos epsilon
# Con este tipo de algoritmo no podemos ser exactos y rápidos a la vez, mientras mas pequeño sea epsilon es más exacta la solución

goal = int(input('Ingrese un número'))
epsilon = 0.01
step = epsilon ** 2  # It's less than epsilon
result = 0.0

while abs(result ** 2 - goal) >= epsilon and result <= goal:
    result += step
    print(result)

if abs(result ** 2 - goal) >= epsilon:
    print(f'No encontramos una raiz para {goal}')
else:
    print(f'La raiz de {goal} es {result}')
