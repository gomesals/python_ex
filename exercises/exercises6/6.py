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

def data_por_extenso(dia, mes, ano):
  return '{0} de {1} de {2}'.format(dia, meses[mes], ano)


data = 'a'

while data != '':
  data = input('Data de Nascimento: ')
  if data == '':
    exit()

  try:
    dia, mes, ano = data.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
  except:
    print('Data inválida')
    continue

  extenso = data_por_extenso(dia, mes, ano)
  print('Você nasceu em', extenso)