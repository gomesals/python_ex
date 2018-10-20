class Macaco:
    nome = ''

    def __init__(self, nome=''):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop()

macaco1 = Macaco('macaco 1')
macaco2 = Macaco('macaco 2')

macaco1.comer('Sopa')
macaco2.comer('Macarrão')

macaco1.verBucho()
macaco2.verBucho()

macaco1.comer(macaco2)

macaco1.verBucho()
