def valorPagamento(prestacao, atraso):
  if atraso == 0:
    return prestacao
  multa = prestacao * 0.03
  juros = prestacao * atraso * 0.001
  return round(prestacao + multa + juros, 2)


valor = -1

quantidade = 0
valorTotal = 0

while valor != 0:
  valor = float(input('Valor: R$ '))
  if valor == 0:
    continue

  atraso = int(input('Dias em atraso: '))

  novoValor = valorPagamento(valor, atraso)
  quantidade += 1
  valorTotal += novoValor
  print('Valor a ser pago: R$', novoValor)

print('Pagos no dia:', quantidade)
print('Valor total: R$', round(valorTotal, 2))