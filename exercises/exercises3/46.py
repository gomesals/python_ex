nome = ' '


while nome != '':
  nome = input('Atleta: ')
  if nome == '':
    exit()

  melhor = 0
  pior = 0
  media = 0

  print('')
  salto1 = float(input('Primeiro Salto: '))
  salto2 = float(input('Segundo Salto: '))
  salto3 = float(input('Terceiro Salto: '))
  salto4 = float(input('Quarto Salto: '))
  salto5 = float(input('Quinto Salto: '))

  melhor = salto1
  pior = salto1

  if salto2 > melhor:
    melhor = salto2
  if salto3 > melhor:
    melhor = salto3
  if salto4 > melhor:
    melhor = salto4
  if salto5 > melhor:
    melhor = salto5
  
  if salto2 < pior:
    pior = salto2
  if salto3 < pior:
    pior = salto3
  if salto4 < pior:
    pior = salto4
  if salto5 < pior:
    pior = salto5

  media = salto1 + salto2 + salto3 + salto4 + salto5 - melhor - pior
  media = round(media / 3, 2)

  print('Melhor salto:', melhor, 'm')
  print('Pior salto:', pior, 'm')
  print('Média dos demais saltos:', media, 'm')
  print('')
  print('Resultado final:')
  print(nome, ':', media, 'm')
