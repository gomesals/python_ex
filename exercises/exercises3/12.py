n = 0

while n < 1 or n > 10:
  n = int(input('Informe o número para gerar a tabuada: '))

print('Tabuada de', n, ':')

for i in range(1, 11):
  print(n, 'x', i, '=', n * i)