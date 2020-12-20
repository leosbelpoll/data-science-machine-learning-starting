def search(lista, objetivo):
    pos = len(lista) // 2

    if len(lista) == 0:
        return False
    if lista[pos] == objetivo:
        return True
    if lista[pos] > objetivo:
        return search(lista[:pos - 1], objetivo)
    return search(lista[pos + 1:], objetivo)


if __name__ == '__main__':
    print(search([1, 2, 3, 4, 5, 6, 7], 2))
