x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))

maiores = []

maior = x

maiores.append(maior)

if y >= maior:
  maior = y
  maiores.append(maiores[0])
  maiores[0] = maior
else:
  maiores.append(y)
  
if z >= maior:
  maior = z
  maiores.append(maiores[1])
  maiores[1] = maiores[0]
  maiores[0] = maior
else:
  maiores.append(z)

for number in maiores:
  print(number)
