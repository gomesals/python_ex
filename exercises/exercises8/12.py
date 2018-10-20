class ContaInvestimento:
    numero = 0
    nome = ''
    saldo = 0.0
    taxaJuros = 0

    def __init__(self, numero, nome, saldo=0, taxa=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.taxaJuros = taxa

    def alterarNome(self, nome): self.nome = nome

    def deposito(self, valor): self.saldo += valor

    def saque(self, valor): self.saldo -= valor

    def adicioneJuros(self):
        self.taxaJuros += 10
        juros = self.taxaJuros / 100
        juros += 1
        self.saldo = self.saldo * juros


def log(conta):
    print('____')
    print('numero', conta.numero)
    print('nome', conta.nome)
    print('saldo', conta.saldo)


banco = ContaInvestimento(150, 'Alexandre', 1000)

log(banco)

banco.adicioneJuros()
banco.adicioneJuros()
banco.adicioneJuros()
banco.adicioneJuros()
banco.adicioneJuros()

log(banco)
