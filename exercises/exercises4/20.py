print('Projeção de Gastos com Abono')
print('============================')
print('')

salario = -1

total = 0
totalMinimo = 0

valorTotalAbono = 0
maiorValorAbono = 0
valores = []

while salario != 0:
  salario = int(input('Salário: '))
  if salario == 0:
    continue

  if salario <= 500:
    totalMinimo += 1
    abono = 100
  else:
    abono = salario * 0.2

  if abono > maiorValorAbono:
    maiorValorAbono = abono

  valorTotalAbono += abono

  valores.append([salario, abono])

  total += 1

print('')
print('{0:10} - {1:10}'.format('Salário', 'Abono'))

for valor in valores:
  print('R$ {0:10} - R$ {1:10}'.format(valor[0], valor[1]))

print('')
print('Foram processados', total, 'colaboradores')
print('Total gasto com abono: R$', valorTotalAbono)
print('Valor mínimo pago a', totalMinimo, 'colaboradores')
print('Maior valor de abono pago: R$', maiorValorAbono)