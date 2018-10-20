nome = ' '

while nome != '':
  nome = input('Atleta: ')
  if nome == '':
    exit()

  media = 0
  saltos = []

  print('')
  saltos.append(float(input('Primeiro Salto: ')))
  saltos.append(float(input('Segundo Salto: ')))
  saltos.append(float(input('Terceiro Salto: ')))
  saltos.append(float(input('Quarto Salto: ')))
  saltos.append(float(input('Quinto Salto: ')))

  print('Resultado final:')
  print('Atleta:', nome)
  print('Saltos:', end=' ')
  
  for index, salto in enumerate(saltos):
    media += salto
    print(salto, end=" ")
    if index < len(saltos):
      print(' - ', end='')
  
  print('')

  media = round(media / len(saltos), 2)
  print('Média dos saltos:', media, 'm')
