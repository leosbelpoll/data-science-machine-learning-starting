def ordenar(lista):
    temp = lista.copy()
    n = len(temp)

    for i in range(1, n):
        current_position = i

        while current_position > 0 and temp[current_position] < temp[current_position - 1]:
            temp[current_position],
            temp[current_position - 1] = temp[current_position -
                                              1], temp[current_position]
            current_position -= 1

    return temp


if __name__ == '__main__':
    print(ordenar([6, 3, 8, 3, 6, 2, 7, 9, 12, 45, 126, 678, 4, 734, 23]))
