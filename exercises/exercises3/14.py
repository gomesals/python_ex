numeros = []

while len(numeros) < 10:
  numeros.append(int(input('Informe um número: ')))

pares = 0
impares = 0

for num in numeros:
  if num % 2 == 0:
    pares += 1
  else:
    impares += 1

print('Pares:', pares)
print('Impares:', impares)