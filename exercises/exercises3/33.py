n = int(input('Quantidade de temperaturas: '))

temperaturas = []

maior = 0
menor = 0

total = 0

while len(temperaturas) < n:
  temp = float(input(': '))
  if len(temperaturas) == 0:
    menor = temp
    maior = temp

  if temp > maior:
    maior = temp
  if temp < menor:
    menor = temp

  temperaturas.append(temp)
  total += temp

print('Maior', maior)
print('Menor', menor)
print('Média', total / n)