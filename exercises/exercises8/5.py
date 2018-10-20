class ContaCorrente:
    numero = 0
    nome = ''
    saldo = 0.0

    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome): self.nome = nome

    def deposito(self, valor): self.saldo += valor

    def saque(self, valor): self.saldo -= valor


def log(conta):
    print('____')
    print('numero', conta.numero)
    print('nome', conta.nome)
    print('saldo', conta.saldo)


banco = ContaCorrente(150, 'Alexandre', 100)

log(banco)

banco.deposito(300.50)

log(banco)

banco.saque(50.250)

log(banco)
