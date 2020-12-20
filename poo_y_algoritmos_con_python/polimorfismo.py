class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando en bici')


if __name__ == '__main__':
    persona = Persona('Juan')
    persona.avanza()

    ciclista = Ciclista('Pedro')
    ciclista.avanza()
