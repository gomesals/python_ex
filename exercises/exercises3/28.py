n = int(input('Quntidade de CDs: '))

cds = []
somatorio = 0

while len(cds) < n:
  cd = float(input('Valor do CD: '))
  somatorio += cd
  cds.append(cd)

print('Total investido: R$ ', somatorio)
print('Preço médio: R$', round(somatorio / n, 2))