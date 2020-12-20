import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_barajas():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamanno_mano):
    return random.sample(barajas, tamanno_mano)

def main(numero_barajas_mano, numero_intentos):
    barajas = crear_barajas()

    cantidad_evento_correcto = 0

    for _ in range(numero_intentos):
        mano = obtener_mano(barajas, numero_barajas_mano)
        valores = [carta[1] for carta in mano]
        cantidades = dict(collections.Counter(valores))
        for cantidad in cantidades.values():
            if cantidad == 2:
                cantidad_evento_correcto += 1
                break

    probabilidad = cantidad_evento_correcto / numero_intentos
    print(f'Hay una probabilidad de {probabilidad}')


if __name__ == '__main__':
    numero_barajas_mano = 5
    numero_intentos = 100000

    main(numero_barajas_mano, numero_intentos)

