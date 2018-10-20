n = int(input('Quantidade de notas: '))

notas = []
somatorio = 0


while len(notas) < n:
  nota = float(input(': '))
  notas.append(nota)
  somatorio += nota

media = somatorio / len(notas)
print('Média:', media)