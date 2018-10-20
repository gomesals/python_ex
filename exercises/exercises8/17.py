import random


class Tamagushi:

    def __init__(self):
        self.nome = ''
        self.fome = random.randint(10, 20)
        self.saude = 0
        self.idade = 0
        self.tedio = (random.randint(0, 1)) / 100

    def retornarHumor(self): return (self.retornarFome() +
                                     self.retornarSaude()) * self.tedio

    def alterarNome(self, nome): self.nome = nome

    def alterarFome(self, fome): self.fome = fome

    def alterarSaude(self, saude): self.saude = saude

    def alterarIdade(self, idade): self.idade = idade

    def retornarNome(self): return self.nome

    def retornarFome(self): return self.fome

    def retornarSaude(self): return self.saude

    def retornarIdade(self): return self.idade

    def darComida(self, comida): self.fome -= comida

    def brincar(self, tempo): self.tedio -= tempo / 100


class Fazenda:
    pets = []

    def __init__(self):
        pass

    def adiciona(self, pet): self.pets.append(pet)

    def retornaPets(self): return self.pets

    def alimentarTodos(self, comida):
        for pet in self.pets:
            pet.darComida(comida)

    def brincarTodos(self, tempo):
        for pet in self.pets:
            pet.brincar(tempo)

fazenda = Fazenda()

pet1 = Tamagushi()
fazenda.adiciona(pet1)

pet1.nome = 'pet 1'
pet1.alterarSaude(3)
pet1.darComida(3)

pet2 = Tamagushi()
fazenda.adiciona(pet2)

pet2.nome = 'pet 2'
pet2.alterarSaude(1)
pet2.darComida(5)


pets = fazenda.retornaPets()

print('Fome')

print(pets[0].fome)
print(pets[1].fome)

fazenda.alimentarTodos(2)

print(pets[0].fome)
print(pets[1].fome)

print('Tédio')

print(pets[0].tedio)
print(pets[1].tedio)

fazenda.brincarTodos(20)

print(pets[0].tedio)
print(pets[1].tedio)
