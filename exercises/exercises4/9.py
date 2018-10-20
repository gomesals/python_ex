n = []

while len(n) < 10:
  n.append(int(input('Número: ')))

quadrados = [x ** 2 for x in n]

soma = 0

for i in quadrados:
  soma += i

print('Soma:', soma)