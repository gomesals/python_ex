n = 0

intervalos = [['[0-25]', 0], ['[26-50]', 0], ['[51-75]', 0], ['[76-100]', 0]]

while n >= 0:
  n = int(input('Informe um número: '))
  if n < 0:
    break;

  if n <= 25:
    intervalos[0][1] += 1
  elif n > 25 and n <= 50:
    intervalos[1][1] += 1
  elif n > 50 and n <= 75:
    intervalos[2][1] += 1
  else:
    intervalos[3][1] += 1

for i in intervalos:
  print(i[0], i[1])