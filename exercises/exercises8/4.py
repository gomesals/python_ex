class Pessoa:
    nome = ''
    idade = 0
    peso = 0.0
    altura = 0.0

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.05
        self.idade += 1

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


eu = Pessoa()
eu.nome = 'Alexandre'


def log(pessoa):
    print('nome', pessoa.nome)
    print('idade', pessoa.idade)
    print('peso', pessoa.peso)
    print('altura', pessoa.altura)

log(eu)

eu.crescer(1.6)

log(eu)

eu.engordar(66.5)

log(eu)

eu.envelhecer()
eu.envelhecer()
eu.envelhecer()

log(eu)
