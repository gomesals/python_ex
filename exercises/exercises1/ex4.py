notas = []

notas.append(float(input('Insira a nota 1º bimestre: ')))
notas.append(float(input('Insira a nota 2º bimestre: ')))
notas.append(float(input('Insira a nota 3º bimestre: ')))
notas.append(float(input('Insira a nota 4º bimestre: ')))

media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4

print('Média:', media)