morangos = float(input('Quantidade de morango (em Kg): '))
maca = float(input('Quantidade de maçã (em Kg): '))

if morangos < 5:
  precoMorangos = morangos * 2.5
else:
  precoMorangos = morangos * 2.2

if maca < 5:
  precoMaca = maca * 1.8
else:
  precoMaca = maca * 1.5


totalPeso = morangos + maca
totalPreco = precoMaca + precoMorangos

if totalPreco > 25 or totalPeso > 8:
  totalPreco = totalPreco * 0.9

totalPreco = round(totalPreco, 2)

print('Valor a ser pago:', 'R$', totalPreco)
