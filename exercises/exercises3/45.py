temAluno = True

gabarito = {}

p = 1
while p <= 10:
  gabarito[p] = input(str(p) + ' - Resposta: ').lower()
  p += 1

print(gabarito)

somatorioPontos = 0
totalAlunos = 1
maior = -1
menor = 11

while temAluno:
  n = 1
  respostas = 0
  while n <= 10:
    resposta = input(str(n) + '): ').lower()
    if resposta == gabarito.get(n):
      somatorioPontos += 1
      respostas += 1
    n += 1

    if respostas > maior:
      maior = respostas

    if respostas < menor:
      menor = respostas

  novoAluno = input('Tem mais algum aluno para responder? S-Sim, N-Não: ').lower()

  if novoAluno == 's':
    temAluno = True
    totalAlunos += 1
  else:
    temAluno = False


print('Maior:', maior)
print('Menor:', menor)
print('Total de alunos:', totalAlunos)
print('Média:', somatorioPontos / totalAlunos)