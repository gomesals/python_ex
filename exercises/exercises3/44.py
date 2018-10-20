print('1 , 2, 3, 4  - Votos para os respectivos candidatos ')
print('1 - Nora')
print('2 - Kanesha')
print('3 - Johnson')
print('4 - Ilona')
print('5 - Voto Nulo')
print('6 - Voto em Branco')

voto = -1

contagem = [0,0,0,0,0,0]
total = 0

while voto != 0:
  voto = int(input(': '))
  if voto > 6 or voto < 0:
    continue
  if voto == 0:
    break
  total += 1
  contagem[voto - 1] += 1

for i in range(0, 4):
  print('Candidato ', i + 1, ':', contagem[i], 'votos')

print('Votos nulos: ', contagem[4])
print('Votos em branco: ', contagem[5])

nulosPercent = round((100 * contagem[4]) / total, 2)
brancoPercent = round((100 * contagem[5]) / total, 2)

print('Votos nulos / total de votos (%):', nulosPercent)
print('Votos em branco / total de votos (%):', brancoPercent)