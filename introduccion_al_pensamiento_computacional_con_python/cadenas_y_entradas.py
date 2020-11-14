# Cadenas

print('123')
print('123' * 3)
print('123' + '456')
print('Hip ' * 3 + ' ' + 'hurra')
print(f'{"Hip " * 3} hurra')

print(len('Hello world'))
my_var = 'Buy world'
print(len(my_var))

print(my_var[0])
print(my_var[1])
print(my_var[2])

print(my_var[4:])
print(my_var[:5])

print(my_var[:-3])
print(my_var[::2])

my_name = 'Leo'
print('Mi nombre es ' + my_name)
print(f'Mi nombre es {my_name}')
print(f'Mi nombre es {my_name} ' * 5)

frase = 'python es un gran lenguaje'

print(frase.count('e'))
print(frase.replace('p', 'q'))
print(frase.split(' '))
print(frase.title())
print(frase.capitalize())


# Entradas
name = input('Cuál es tu nombre? ')
print(f'Tu nombre es: {name}')

numero = input('Escribe un número ')
numero = int(numero)

print(f'La suma con 10 es: {numero + 10}')
