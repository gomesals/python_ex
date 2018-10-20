x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))

maior = x

if y > maior:
  maior = y

if z > maior:
  maior = z

print(maior)