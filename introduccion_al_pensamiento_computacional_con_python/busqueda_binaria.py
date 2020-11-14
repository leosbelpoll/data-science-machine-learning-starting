# cuando la respuesta se encuentra en un conjunto ordenado, podemos utilizar búsqueda binaria
# es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración

goal = int(input('Ingrese un número'))
epsilon = 0.01
min_limit = 0.0
max_limit = max(1.0, goal)
result = (max_limit + min_limit) / 2

while abs(result ** 2 - goal) >= epsilon:
    if result ** 2 > goal:
        max_limit = result
    else:
        min_limit = result

    result = (max_limit + min_limit) / 2

print(f'La raiz es {result}')
