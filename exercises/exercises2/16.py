a = int(input('Insira o valor de a: '))

if a == 0:
  print('Equação não é de segundo grau')
  exit()

b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
  print('Delta negativo, a equação não possui raízes reais')
elif delta == 0:
  print('Delta igual a 0, possuindo somente uma raiz real')
  raiz = (-b) / (2 * a)
  print('Raiz:', raiz)
else:
  raiz1 = ((-b) + (delta ** 0.5)) / (2 * a)
  raiz2 = ((-b) - (delta ** 0.5)) / (2 * a)
  print('Raiz 1:', raiz1)
  print('Raiz 2:', raiz2)