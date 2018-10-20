qtt = int(input('Quantidade de pessoas: '))

pessoas = []
somatorio = 0

while len(pessoas) < qtt:
  pessoa = int(input('Idade: '))
  pessoas.append(pessoa)
  somatorio += pessoa

media = somatorio / len(pessoas)

if media <= 25:
  print('Jovem')
elif media > 25 and media < 60:
  print('Adulta')
else:
  print('Idosa')