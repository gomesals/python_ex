class BombaCombustivel:
    tipoCombustivel = ''
    valorLitro = 0.0
    quantidadeCombustivel = 0

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - litros)
        print('Litros abastecidos:', round(litros, 2))

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro
        print('Valor a ser pago: R$', valor)
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - litros)
        pass

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, combustivel):
        self.combustivel = combustivel

    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidadeCombustivel = quantidade


posto = BombaCombustivel()
posto.alterarCombustivel('Gasolina')
posto.alterarValor(3.5)
posto.alterarQuantidadeCombustivel(100)


posto.abastecerPorLitro(10)
posto.abastecerPorValor(35)
