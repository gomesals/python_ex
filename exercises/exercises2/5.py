notas = []
notas.append(float(input('Digite a nota 1: ')))
notas.append(float(input('Digite a nota 2: ')))

media = (notas[0] + notas[1]) / 2

if media < 7:
  print('Reprovado')
elif media >= 7 and media < 10:
  print('Aprovado')
else:
  print('Aprovado com Distinção')