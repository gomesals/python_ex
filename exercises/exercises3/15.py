n = int(input('Informe um número inteiro maior que zero: '))

a, b = 1, 1

termos = 0
while termos < n:
  print(a, end=" ")
  c = a + b
  a = b
  b = c
  termos += 1