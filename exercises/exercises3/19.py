n = -1

while n < 0 or n > 1000:
  n = int(input('Informe a quantidade de números: '))

numeros = []

count = 0

maior = -1
menor = -1

while count < n:
  valor = -1
  while valor < 0 or valor > 1000:
    valor = int(input(': '))

  if maior == -1:
    maior = valor

  if menor == -1:
    menor = valor

  if valor > maior:
    maior = valor

  if valor < menor:
    menor = valor

  numeros.append(valor)
  count += 1

print('Menor', menor)
print('Maior', maior)

resultado = 0

for i in numeros:
  resultado += i

print('Soma', resultado)