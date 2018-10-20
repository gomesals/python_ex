

class Class1:
    """ Class example """
    i = 123

    def __init__(self):
        print('Construtor...')
        self.data = []

    def f(self):
        return 'Hello world from first class!'


class Operacoes:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x): self.x = x

    def set_y(self, y): self.x = y

    def soma(self): return self.x + self.y

classe = Class1()

print(classe.i)
print(classe.f())

print(Class1().f())
print('----')

matematica = Operacoes(3, 5)
print(matematica.soma())
matematica.set_x(5)
print(matematica.soma())
