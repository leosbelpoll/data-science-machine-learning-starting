import random
import math
from estadisticas import media, desviacion_estandar

def lanzar_agujas(numero_agujas):
    cantidad_dentro_circulo = 0

    for _ in range(numero_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_centro = math.sqrt(x ** 2 + y ** 2)

        if distancia_desde_centro <= 1:
            cantidad_dentro_circulo += 1

    return 4 * cantidad_dentro_circulo / numero_agujas


def estimacion(numero_agujas, numero_intentos):
    estimados = []
    for _ in range(numero_intentos):
        estimacion_pi = lanzar_agujas(numero_agujas)
        estimados.append(estimacion_pi)

    _media = media(estimados)
    _sigma = desviacion_estandar(estimados)

    print(f'Media {_media}')
    print(f'Desviacion estandar {_sigma}')

    return (_media, _sigma)

def estimar_pi(precision, numero_intentos):
    numero_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_agujas, numero_intentos)
        numero_agujas *= 2

    return media


if __name__ == '__main__':
    estimar_pi(0.01, 1000)

