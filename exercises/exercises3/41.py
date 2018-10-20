divida = float(input('Valor da dívida: R$ '))

taxas = [[1, 0], [3, 10], [6, 15], [9, 20], [12, 25]]

print('Valor da Dívida', 'Valor dos Juros', 'Quantidade de Parcelas', 'Valor da Parcela')

for opcao in taxas:
  juros = opcao[1] / 100
  juros = divida * juros
  valor = divida + juros
  # print(juros)
  print('R$', valor, '      R$', juros, '        ', opcao[0], '            R$', round(valor / opcao[0], 2))