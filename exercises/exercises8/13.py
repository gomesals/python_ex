class Funcionario:
    nome = ''
    salario = 0.0

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def retornarNome(self): return self.nome

    def retornarSalario(self): return self.salario


f1 = Funcionario('Alexandre', 100)
f2 = Funcionario('Gomes', 80)

print(f1.retornarNome(), f1.retornarSalario())
print(f2.retornarNome(), f2.retornarSalario())
