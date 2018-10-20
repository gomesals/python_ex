tabuada = int(input('Montar a tabuada de: '))
comecar = int(input('Começar por: '))
terminar = comecar - 1

while terminar < comecar:
  terminar = int(input('Terminar em: '))

print()
print('Vou montar a tabuada de', tabuada, 'começando em', comecar, 'e terminando em', str(terminar) + ':')

for i in range(comecar, terminar + 1):
  print(tabuada, 'X', i, '=', tabuada * i)