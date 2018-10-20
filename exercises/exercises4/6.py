alunos = 0
medias = []

while alunos < 4:
  media = 0
  notas = 0
  print('Aluno', str(alunos + 1))
  while notas < 4:
    media += float(input('Nota ' + str(notas + 1) + ': '))
    notas += 1
  media = media / 4
  if media >= 7:
    medias.append(media)
  alunos += 1

print('Alunos com nota >= 7:', str(len(medias)))