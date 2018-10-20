class Veiculo:
    # buzina = ''

    def __init__(self):
        self.rodas = 0
        # self.buzina = ''

    def dirigir(self):
        print('Dirigindo com', self.rodas, 'rodas')

    def buzinar(self):
        print('Buzina:', self.buzina)

    def abastecer(self):
        print('Abastecendo um veículo')


class Moto(Veiculo):
    rodas = 2
    buzina = 'Bii'

    def __init__(self):
        Veiculo.rodas = self.rodas
        Veiculo.buzina = self.buzina

    def abastecer(self):
        print('Abastecendo a moto')


class Carro(Veiculo):
    rodas = 4
    buzina = 'Bann'

    def __init__(self):
        Veiculo.rodas = self.rodas
        Veiculo.buzina = self.buzina

    def abastecer(self):
        print('Abastecendo o carro')

motinha = Moto()
carrinho = Carro()

motinha.dirigir()
motinha.buzinar()
motinha.abastecer()

print('----')

carrinho.dirigir()
carrinho.buzinar()
carrinho.abastecer()
