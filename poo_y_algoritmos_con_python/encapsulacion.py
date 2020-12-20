class CasillaVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        # some logic
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(
                f'La region {region} no se encuentra en el listado de regiones')


if __name__ == '__main__':
    casilla = CasillaVotacion(1, ['Santiago', 'Cienfuegos', 'Habana'])
    print(casilla.region)
    casilla.region = 'Santiago'
    print(casilla.region)

    try:
        casilla.region = 'Desconocida'
    except ValueError as e:
        print(str(e))
