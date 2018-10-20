n = int(input('Quantidade de turmas: '))

turmas = []
somatorio = 0

while len(turmas) < n:
  turma = -1
  while turma < 0 or turma > 40:
    turma = int(input('Alunos: '))
  turmas.append(turma)
  somatorio += turma

media = round(somatorio / n, 2)

print('Média', media)