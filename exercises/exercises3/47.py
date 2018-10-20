nome = ' '


while nome != '':
  nome = input('Atleta: ')
  if nome == '':
    exit()

  media = 0
  notas = []

  while len(notas) < 7:
    notas.append(float(input('Nota: ')))

  media = 0
  melhor = notas[0]
  pior = notas[0]

  for nota in notas:
    media += nota
    if nota > melhor:
      melhor = nota
    if nota < pior:
      pior = nota

  media = media - melhor - pior
  media = round(media / 5, 2)

  print('')
  print('Resultado final:')
  print('Atleta:', nome)
  print('Melhor nota:', melhor)
  print('Pior nota:', pior)
  print('Média:', media)