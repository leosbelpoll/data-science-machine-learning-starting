import random
import math

def media(valores):
    return sum(valores) / len(valores)

def varianza(valores):
    mu = media(valores)

    acumulador = 0
    for x in valores:
        acumulador += (x - mu) ** 2

    return acumulador / len(valores)

def desviacion_estandar(valores):
    return math.sqrt(varianza(valores))

if __name__ == '__main__':
    valores = [random.randint(1, 21) for i in range(20)]
    #valores = [random.randint(9, 12) for i in range(20)]

    _media = media(valores)
    _varianza = varianza(valores)
    _desviacion = desviacion_estandar(valores)

    print(f'valores {valores}')
    print(f'media {_media}')
    print(f'varianza {_varianza}')
    print(f'desviacion {_desviacion}')

