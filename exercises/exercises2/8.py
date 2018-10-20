x = float(input('Digite o valor do primeiro produto: '))
y = float(input('Digite o valor do segundo produto: '))
z = float(input('Digite o valor do terceiro produto: '))

menor = x
produto = 'primeiro'

if y < menor:
  menor = y
  produto = 'segundo'

if z < menor:
  menor = z
  produto = 'terceiro'

print('Você deve comprar o', produto, 'produto')
