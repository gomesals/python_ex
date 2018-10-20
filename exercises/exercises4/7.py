n = []

while len(n) < 5:
  n.append(int(input('Número: ')))

soma = 0
multiplicacao = 1
for i in n:
  soma += i
  multiplicacao *= i

print('Soma:', soma)
print('Multiplicação:', multiplicacao)
print(n)