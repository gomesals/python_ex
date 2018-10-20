p = []

while len(p) < 5:
  idade = int(input('idade: '))
  altura = int(input('Altura: '))
  p.append([idade, altura])

p.reverse()
print(p)