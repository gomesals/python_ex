# n = int(input('Informe um número inteiro: '))
n = 10

primos = [2]


for i in range(2, n + 1):
  divisor = 2
  while divisor < i:
    if i == divisor:
      divisor += 1
      continue
    if i % divisor == 0:
      break
    print('-', i)
    divisor += 1
  print(i)

# while 

# while divisor < n:
#   if n % divisor == 0:
#     print(n, 'é divisível por', divisor)
#     isPrime = False
#   divisor += 1

# if isPrime:
#   print(n, 'é primo')
# else:
#   print(n, 'não é primo')