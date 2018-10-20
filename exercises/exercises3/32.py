n = int(input('Informe um número: '))
fatorial = 1

print('Fatorial de', n)
print(str(n) + '! = ', end = " ")

while n > 0:
  fatorial *= n
  print(n, end=" ")
  if n > 1:
    print('.', end=" ")
  n -= 1

print('=', fatorial)