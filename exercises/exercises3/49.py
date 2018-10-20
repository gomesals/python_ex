n = int(input('Informe o valor de n: '))

print('S = ', end = "")

denominador = 1
for i in range(1, n + 1):
  valor = str(i) + '/' + str(denominador)
  print(valor, end = "")
  if i != n:
    print(' +', end=" ")
  else:
    print('.')
  denominador += 2
