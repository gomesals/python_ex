PRECO = 1.99

print('Lojas Quase Dois - Tabela de preços')

for i in range(1, 51):
  valor = i * PRECO
  valor = '%.2f' % valor
  print(i, '- R$', valor)