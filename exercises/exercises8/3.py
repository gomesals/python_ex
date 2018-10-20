class Retangulo:
    base = 0
    altura = 0

    def mudarLado(self, base, altura):
        self.base = base
        self.altura = altura

    def retornarLado(self):
        return {
            base: self.base,
            altura: self.altura
        }

    def calcularArea(self):
        self.area = self.base * self.altura
        return self.area

    def calcularPerimetro(self):
        self.perimetro = (self.base + self.altura) * 2
        return self.perimetro


altura = int(input('Largura: '))
base = int(input('Comprimento: '))

local = Retangulo()

local.mudarLado(base, altura)

print('Pisos:', local.calcularArea())
print('Rodapé:', local.calcularPerimetro())
