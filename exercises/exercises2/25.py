print('Responda as questões informando \'s\' para sim, e \'n\' para não')

a = input('Telefonou para a vítima? ').lower()
b = input('Esteve no local do crime? ').lower()
c = input('Mora perto da vítima? ').lower()
d = input('Devia para a vítima? ').lower()
e = input('Já trabalhou com a vítima? ').lower()

def conta_pontos(letra):
  if letra == 's' or letra == 'sim':
    return 1
  return 0

pontos = 0

pontos += conta_pontos(a)
pontos += conta_pontos(b)
pontos += conta_pontos(c)
pontos += conta_pontos(d)
pontos += conta_pontos(e)


if pontos == 2:
  print('Suspeita')
elif pontos > 2 and pontos <= 4:
  print('Cúmplice')
elif pontos == 5:
  print('Assassino')
else:
  print('Inocente')
