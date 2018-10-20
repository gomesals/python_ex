class Ponto:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprime(self):
        print('x', self.x, 'y', self.y)


class Retangulo:

    def __init__(self, altura, largura, partida):
        self.altura = altura
        self.largura = largura
        self.partida = partida

    def alterarAltura(self, altura):
        self.altura = altura

    def alterarLargura(self, largura):
        self.largura = largura

    def centro(self):
        y = self.altura / 2
        x = self.largura / 2
        return Ponto(y, x)

x1y1 = Ponto(1, 1)
x1y10 = Ponto(1, 10)

r1 = Retangulo(6, 8, x1y1)
r2 = Retangulo(10, 4, x1y1)
r3 = Retangulo(7, 7, x1y10)

print(r1.altura)
print(r1.largura)
r1.centro().imprime()

print('----')

print(r3.largura)
print(r3.altura)
r3.centro().imprime()
