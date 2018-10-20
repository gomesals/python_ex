meses = {
  1: 'Janeiro',
  2: 'Fevereiro',
  3: 'Março',
  4: 'Abril',
  5: 'Maio',
  6: 'Junho',
  7: 'Julho',
  8: 'Agosto',
  9: 'Setembro',
  10: 'Outubro',
  11: 'Novembro',
  12: 'Dezembro'
}

temperaturas = []

media = 0

print(len(meses))

while len(temperaturas) < len(meses):
  question = 'Temperatura para ' + meses[len(temperaturas) + 1] + ': '
  temperatura = float(input(question))
  temperaturas.append([len(temperaturas), temperatura])
  media += temperatura

media = round(media / len(meses), 2)

mesesAcimaMedia = [mes for mes in temperaturas if mes[1] > media]

for i in mesesAcimaMedia:
  print(meses[i[0] + 1], ':', i[1])
