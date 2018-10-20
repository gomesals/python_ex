x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))

maior = x
menor = x

if y >= maior:
  maior = y
else:
  menor = y

if z >= maior:
  maior = z
else:
  menor = z

print('Maior:', maior)
print('Menor:', menor)