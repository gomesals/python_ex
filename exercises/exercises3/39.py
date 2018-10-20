n = 0

maisAlto = 0
maisBaixo = 0

maisAltoC = 0
maisBaixoC = 0


while n < 2:
  aluno = input('Informe número e altura do aluno (em cm), separados por espaço: ')
  numero, altura = aluno.split(' ')

  if n == 0:
    maisAlto = altura
    maisBaixo = altura
    maisBaixoC = numero
    maisAltoC = numero

  if altura > maisAlto:
    maisAlto = altura
    maisAltoC = numero
  else:
    maisBaixo = altura
    maisBaixoC = numero

  n += 1

print('Mais alto: ', maisAltoC, '-', maisAlto)
print('Mais baixo: ', maisBaixoC, '-', maisBaixo)