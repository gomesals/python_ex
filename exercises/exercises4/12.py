alunos = []
mediaAltura = 0

while len(alunos) < 5:
  idade = int(input('Idade: '))
  altura = int(input('Altura: '))

  alunos.append([idade, altura])
  mediaAltura += altura

mediaAltura = round(mediaAltura / len(alunos), 2)

alunosMais13Anos = [x for x in alunos if x[0] > 13]

alunosBuscados = [x for x in alunosMais13Anos if x[1] < mediaAltura]

print('Alunos:', str(len(alunosBuscados)))