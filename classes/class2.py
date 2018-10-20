class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

fido = Dog('Fido')
dido = Dog('Dido')

fido.add_trick('Latir')
dido.add_trick('Correr')

print(fido.tricks)
print(dido.tricks)

print('----')


class DogOk:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

fido = DogOk('Fido')
dido = DogOk('Dido')

fido.add_trick('Latir')
dido.add_trick('Correr')

print(fido.tricks)
print(dido.tricks)
