class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'resposo'
        self._motor = Motor(4)

    def acelera(modo='lento'):
        if modo == 'rapido':
            self._motor.injectar_gasolina(10)
        else:
            self._motor.injectar_gasolina(3)


class Motor:

    def __init__(self, numero_cilindros):
        self.numero_cilindros = numero_cilindros
        self._gasolina = 0

    def injectar_gasolina(self, cantidad_gasolina):
        self._gasolina += cantidad_gasolina


if __name__ == '__main__':
    auto1 = Automovil('Up!', 'VW', 'Gris oscuro')

    print(auto1.modelo)
