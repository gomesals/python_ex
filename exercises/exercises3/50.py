n = int(input('Informe o valor de n: '))

h = 1

denominador = 2
for i in range(1, n):
  valor = str(i) + '/' + str(denominador)
  h = ((denominador/1)*h + i) / 2
  denominador += 1

print('H =', h)
