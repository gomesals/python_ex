nome = input('Nome: ').upper()

contador = len(nome)

for i in range(0, len(nome)):
  print(nome[0:contador])
  contador -= 1
