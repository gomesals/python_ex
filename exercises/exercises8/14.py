class Funcionario:
    nome = ''
    salario = 0.0

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def retornarNome(self): return self.nome

    def retornarSalario(self): return self.salario

    def aumentarSalario(self, percentual):
        aumento = percentual / 100
        aumento += 1
        self.salario *= aumento

f1 = Funcionario('Alexandre', 100)
f2 = Funcionario('Gomes', 80)

print(f1.retornarNome(), f1.retornarSalario())
print(f2.retornarNome(), f2.retornarSalario())

f1.aumentarSalario(10)

print(f1.retornarNome(), f1.retornarSalario())
print(f2.retornarNome(), f2.retornarSalario())
