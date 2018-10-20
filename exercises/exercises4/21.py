GASOLINA = 2.25
DISTANCIA = 1000

modelos = []
consumos = []

menorConsumo = ['', 0]

print('Comparativo de Consumo de Combustível')

while len(modelos) < 5:
  print('Veículo', len(modelos) + 1)
  nome = input('Nome: ')
  consumo = float(input('Consumo: '))
  modelos.append(nome)
  consumos.append(consumo)

  if consumo > menorConsumo[1]:
    menorConsumo[0] = nome
    menorConsumo[1] = consumo

print('')
print('Relatório Final')

for i, value in enumerate(modelos):
  consumoTotal = round(DISTANCIA / consumos[i], 1)
  valorGasolina = round(consumoTotal * GASOLINA, 2)
  print(i + 1, '-', '{0:10}'.format(value), '-', consumos[i], '- ', consumoTotal, 'litros - R$', valorGasolina)

print('O menor consumo é do ', menorConsumo[0])