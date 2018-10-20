print('Quem foi o melhor jogador?')
print('')

jogadores = {}

atual = -1
melhor = [0, 0]
votos = 0

while atual != 0:
  atual = int(input('Número do jogador (0=fim): '))
  if atual < 0 or atual > 23:
    print('Informe um valor entre 1 e 23 ou 0 para sair!')
    continue
  if atual == 0:
    continue

  votos += 1

  if atual in jogadores:
    jogadores[atual] += 1
  else:
    jogadores[atual] = 1

print('')
print('Resultado da votação: ')
print('')
print('Foram computados', votos, 'votos.')
print('')
print('{0:10} {1:8} {2:6}'.format('Jogador', 'Votos', '%'))

for key, value in jogadores.items():
  if value > melhor[1]:
    melhor[0] = key
    melhor[1] = value

  porcentagem = round((value * 100) / votos, 2)
  print('{0:7}    {1:5}  {2:6}%'.format(key, value, porcentagem))


porcentagem = round((melhor[1] * 100) / votos, 2)
print('O melhor jogador da partida foi o número', melhor[0], ', com', melhor[1], 'votos, correspondendo a', porcentagem, '% do total de votos.')