print('Compara duas strings')

string1 = input('String 1: ')
string2 = input('String 2: ')
mesmoTamanho = False

print('Tamanho de "', string1, '":', len(string1), 'caracteres')
print('Tamanho de "', string2, '":', len(string2), 'caracteres')

print('As duas strings são de tamanhos', end=" ")
if len(string1) == len(string2):
  mesmoTamanho = True
  print('iguais')
else:
  print('diferentes')

print('As duas strings possuem conteúdo', end=" ")
if mesmoTamanho:
  if string1 == string2:
    print('iguais')
  else:
    print('diferentes')
else:
  print('diferente.')