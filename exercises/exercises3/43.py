cardapio = {
  100: ['Cachorro Quente', 1.20],
  101: ['Bauru Simples', 1.30],
  102: ['Bauru com ovo', 1.50],
  103: ['Hambúrguer', 1.20],
  104: ['Cheeseburguer', 1.30],
  105: ['Refrigerante', 1.00],
}

codigo = 100

pedidos = []

while codigo >= 100 or codigo <= 105:
  codigo = int(input('Código: '))
  if codigo < 100 or codigo > 105:
    break

  quantidade = int(input('Quantidade: '))

  pedido = cardapio.get(codigo)

  pedidos.append([pedido[0], quantidade, pedido[1]])

print('Especificação', 'Quantidade', 'Valor unitário', 'Valor total')

total = 0

for i in pedidos:
  subtotal = i[1] * i[2]
  print(i[0], i[1], 'R$', i[2], 'R$', subtotal)
  total += subtotal

print('Total: R$', round(total, 2))

# cardapio.filter()

# print(cardapio)
# print(cardapio['le'])

# print(cardapio.get(105, 'nao tem'))