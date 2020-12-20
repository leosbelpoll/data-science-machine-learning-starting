def search(lista, objetivo):
    for index, elemento in enumerate(lista):
        if objetivo == elemento:
            return index

    return -1


if __name__ == '__main__':
    print(search([1, 2, 3, 4, 5, 6, 7], 4))
