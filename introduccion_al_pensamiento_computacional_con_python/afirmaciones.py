def divide_elementos_de_lista(lista, divisor):
    assert divisor != 0, 'El divisor no puede ser cero'
    return [i / divisor for i in lista]


lista = list(range(10))

lista2 = divide_elementos_de_lista(lista, 2)
print(lista2)
