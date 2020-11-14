counter = 0

while counter < 10:
    print(counter)
    counter += 1

print('_' * 100)

external_counter = 0
internal_counter = 0

while external_counter < 5:
    while internal_counter < 6:

        print(f'External: {external_counter}, Internal: {internal_counter}')
        internal_counter += 1
    internal_counter = 0
    external_counter += 1

print('_' * 100)

frutas = ['manzana', 'pera', 'mango']

for fruta in frutas:
    print(f'La siguiente fruta es: {fruta}')

print('_' * 100)

# Iterables: cadenas, listas, tuplas, conjuntos, diccionarios
# a la funcion iter le pasamos un iterable y nos retorna un iterador, el cual podemos usar para un ciclo definido
# cadenas
for letter in iter('Nombre'):
    print(letter)

# listas
for element in iter([1, 2, 3, 4]):
    print(element)

# tuplas
for element in iter((2, 3, 4)):
    print(element)

# conjuntos
for element in iter({'A', 'B', 'C'}):
    print(element)

# diccionarios 1
for element in {'a': 1, 'b': 2, 'c': 3}:
    print(element)

# diccionarios 2
for element in {'a': 1, 'b': 2, 'c': 3}.values():
    print(element)

# diccionarios 3
for element in {'a': 1, 'b': 2, 'c': 3}.keys():
    print(element)

# diccionarios 4
for key, element in {'a': 1, 'b': 2, 'c': 3}.items():
    print(key)
    print(element)
