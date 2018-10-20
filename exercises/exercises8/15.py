class Tamagushi:
    nome = ''
    fome = 0
    saude = 0
    idade = 0
    tedio = 1

    def retornarHumor(self):
        return (self.retornarFome() + self.retornarSaude()) * self.tedio

    def alterarNome(self, nome): self.nome = nome

    def alterarFome(self, fome): self.fome = fome

    def alterarSaude(self, saude): self.saude = saude

    def alterarIdade(self, idade): self.idade = idade

    def retornarNome(self): return self.nome

    def retornarFome(self): return self.fome

    def retornarSaude(self): return self.saude

    def retornarIdade(self): return self.idade

    def darComida(self, comida): self.fome -= comida

    def brincar(self, tempo):
        self.tedio -= tempo / 100

meu = Tamagushi()
meu.nome = 'pet'
meu.alterarFome(10)
meu.alterarSaude(3)

meu.darComida(3)
meu.brincar(20)

print(meu.retornarHumor())
