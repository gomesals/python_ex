n = []

while len(n) < 4:
  n.append(float(input('Nota: ')))


soma = 0
for i, nota in enumerate(n):
  print('Nota', i + 1, ':', nota)
  soma += nota

print('Média:', round(soma / len(n), 2))


