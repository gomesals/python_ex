n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))


soma = 0

for i in range(n1, n2+1):
  print(i)
  soma += i

print('Soma', soma)