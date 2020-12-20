def ordenar(lista):
    lista_temporal = lista.copy()
    longitud = len(lista_temporal)

    for i in range(longitud):
        for j in range(longitud - 1 - i):
            if lista_temporal[j] > lista_temporal[j + 1]:
                lista_temporal[j], lista_temporal[j +
                                                  1] = lista_temporal[j + 1], lista_temporal[j]

    return lista_temporal


if __name__ == '__main__':
    print(ordenar([6, 3, 8, 3, 6, 2, 7, 9, 12, 45, 126, 678, 4, 734, 23]))
