import sys
import random

class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre

class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self, coordenada):
        delta_x = self.x - coordenada.x
        delta_y = self.y - coordenada.y

        return (delta_x ** 2 + delta_y ** 2) ** 0.5

class Campo:
    def __init__(self):
        self.coordenadas_borrachos = {}

    def annadir_borracho(self, borracho, coordenada):
        self.coordenadas_borrachos[borracho] = coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_borrachos[borracho]

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.obtener_coordenada(borracho)
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_borrachos[borracho] = nueva_coordenada

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(nombre='Pepe')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.annadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))


def main(distancias_caminatas, numero_intentos, tipo_borracho):
    for pasos in distancias_caminatas:
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_max = max(distancias)
        distancia_min = min(distancias)

        print(f'Media {distancia_media}')
        print(f'Minima {distancia_min}')
        print(f'Maxima {distancia_max}')

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    distancias_caminatas = [10, 100, 1000, 10000]
    numero_intentos = 100

    main(distancias_caminatas, numero_intentos, BorrachoTradicional)
