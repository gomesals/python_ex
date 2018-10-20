class Tamagushi:
    nome = ''
    fome = 0
    saude = 0
    idade = 0

    def retornarHumor(self):
        return self.retornarFome() + self.retornarSaude()

    def alterarNome(self, nome): self.nome = nome

    def alterarFome(self, fome): self.fome = fome

    def alterarSaude(self, saude): self.saude = saude

    def alterarIdade(self, idade): self.idade = idade

    def retornarNome(self): return self.nome

    def retornarFome(self): return self.fome

    def retornarSaude(self): return self.saude

    def retornarIdade(self): return self.idade

meu = Tamagushi()
meu.nome = 'pet'
meu.alterarFome(10)
meu.alterarSaude(3)

print(meu.retornarHumor())
