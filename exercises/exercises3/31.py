print('Lojas Tabajara')

produto = 1
total = 0
preco = -1
while True:
  while preco != 0:
    preco = float(input('Produto ' + str(produto) + ': R$ '))
    total += preco
    produto += 1

  print('Total: R$', round(total, 2))
  dinheiro = float(input('Dinheiro: R$ '))
  troco = dinheiro - total
  print('Troco: R$', troco)
  
  produto = 1
  total = 0
  preco = -1