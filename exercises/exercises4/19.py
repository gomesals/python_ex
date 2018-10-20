os = {
  1: 'Windows Server',
  2: 'Unix',
  3: 'Linux',
  4: 'Netware',
  5: 'Mac OS',
  6: 'Outro'
}

print('"Qual o melhor Sistema Operacional para uso em servidores?"')
print('')
print('As possíveis respostas são:')
print('')

votos = []

for key, value in os.items():
  votos.append(0)
  print(key, '-', value)
print('')

votos = [1500, 3500, 3000, 500, 150, 150]

voto = 0
total = 8800
# voto = -1
# total = 0
maisVotado = [0, 0]

while voto != 0:
  voto = int(input('Voto: '))

  if voto <= 0 or voto > 6:
    continue

  votos[voto] += 1
  total += 1

print('{0:19}   {1:5}   {2:3}'.format('Sistema Operacional', 'Votos', '%'))
print('-'*19, ' ', '-'*5, ' ', '-'*3)

for key, voto in enumerate(votos):
  if voto > maisVotado[1]:
    maisVotado[0] = key
    maisVotado[1] = voto
  porcentagem = round((voto * 100) / total, 0)
  print('{0:19}   {1:5}   {2:3}'.format(os[key + 1], voto, porcentagem))

print('-'*19, ' ', '-'*5, ' ', '-'*3)
print('{0:19}   {1:5}'.format('Votos', total))

porcentagem = round((maisVotado[1] * 100) / total, 0)
print('O Sistema Operacional mais votado foi o', os[maisVotado[0] + 1], ', com', maisVotado[1], 'votos, correspondendo a', porcentagem, '% do total de votos.')