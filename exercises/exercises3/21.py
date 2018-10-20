n = int(input('Informe um número inteiro: '))


divisor = 2
isPrime = True

while divisor < n:
  if n % divisor == 0:
    isPrime = False
  if not isPrime:
    break
  divisor += 1

if isPrime:
  print(n, 'é primo')
else:
  print(n, 'não é primo')