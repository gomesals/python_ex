class Carro:
    combustivel = 0  # tanque

    def __init__(self, consumo):
        self.consumo = consumo  # km/litros

    def andar(self, distancia):
        litros = distancia / self.consumo
        self.combustivel -= litros

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
print(meuFusca.obterGasolina())
