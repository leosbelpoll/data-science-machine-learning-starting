def morral(tamanno, pesos, valores, posicion):
    if posicion == 0 or tamanno == 0:
        return 0

    if pesos[posicion - 1] > tamanno:
        return morral(tamanno, pesos, valores, posicion - 1)

    return max(valores[posicion - 1] + morral(tamanno - pesos[posicion - 1], pesos, valores, posicion - 1),
               morral(tamanno, pesos, valores, posicion - 1))

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamanno_morral = 50
    posicion = len(valores)

    resultado = morral(tamanno_morral, pesos, valores, posicion)
    print(resultado)

