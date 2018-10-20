n = int(input('Quantidade de eleitores: '))

eleitores = []

candidato = [0, 0, 0]

while len(eleitores) < n:
  eleitor = int(input('Número do candidato (1, 2 ou 3): '))
  eleitores.append(eleitor)
  candidato[eleitor-1] += 1

for c, p in enumerate(candidato):
  print('Candidato', c, ':', p)