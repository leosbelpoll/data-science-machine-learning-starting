class Lavadora:

    def __init__(self, temperatura='caliente'):
        self.temperatura = temperatura

    def lavar(self):
        self._llenar_tanque_de_agua(self.temperatura)
        self._annadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _annadir_jabon(self):
        print('Annadiendo jabon')

    def _lavar(self):
        print('Lavando')

    def _centrifugar(self):
        print('Centrifugando')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
