nota1 = float(input('Insira a nota do 1º Bimestre: '))
nota2 = float(input('Insira a nota do 2º Bimestre: '))

media = round((nota1 + nota2) / 2, 2)

if media > 9 and media <= 10:
  conceito = 'A'
elif media > 7.5 and media <= 9:
  conceito = 'B'
elif media > 6 and media <= 7.5:
  conceito = 'C'
elif media > 4 and media <= 6:
  conceito = 'D'
else:
  conceito = 'E'

print('Nota do 1º Bimestre:', nota1)
print('Nota do 2º Bimestre:', nota2)
print('Média do Bimestre:', media)
print('Conceito:', conceito)

if conceito == 'A' or conceito == 'B' or conceito == 'C':
  print('APROVADO')
else:
  print('REPROVADO')