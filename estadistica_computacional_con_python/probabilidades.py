import random

def tirar_dado(numero_tiros):
    secuencia_tiros = []

    for _ in range(numero_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_tiros.append(tiro)

    return secuencia_tiros


def main(numero_tiros, numero_intentos):
    tiros = []
    for _ in range(numero_intentos):
        secuencia_tiros = tirar_dado(numero_tiros)
        tiros.append(secuencia_tiros)

    tiros_con_1 = 0;
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1

    probabilidad_tiros_1 = tiros_con_1 / numero_intentos
    print(f'La probabilidad es {probabilidad_tiros_1}')

if __name__ == '__main__':
    numero_tiros = 1
    numero_intentos = 10000

    main(numero_tiros, numero_intentos)
