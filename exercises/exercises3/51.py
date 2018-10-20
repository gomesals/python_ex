n = int(input('Informe o valor de n: '))

s = 1
print('S = ', end = "")

denominador = 1
for i in range(1, n + 1):
  valor = str(i) + '/' + str(denominador)
  s = ((denominador/1)*s + i) / 2
  print(valor, end = "")
  
  if i != n:
    print(' +', end=" ")
  else:
    print(' =', end=" ")

  denominador += 2

print(s)
