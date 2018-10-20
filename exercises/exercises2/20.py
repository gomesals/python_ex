nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

media = round((nota1 + nota2 + nota3) / 3, 2)

if media >= 7 and media < 10:
  print('Aprovado. Média:', media)
elif media < 7:
  print('Reprovado. Média:', media)
else:
  print('Aprovado com Distinção.')