preco = float(input('Qual o valor do pão? '))

print('Preço do pão: R$', preco)
print('Panificadora Pão de Ontem - Tabela de preços')

for i in range(1, 51):
  valor = i * preco
  valor = '%.2f' % valor
  print(i, '- R$', valor)