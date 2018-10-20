codigo = -1

mediaAltura = 0
mediaPeso = 0

maisAlto = 0
maisAltoCodigo = 0

maisBaixo = 0
maisBaixoCodigo = 0

maisMagro = 0
maisMagroCodigo = 0

maisGordo = 0
maisGordo = 0

clientes = 0

while codigo != 0:
  codigo = int(input('Código: '))
  if codigo == 0:
    break
  altura = float(input('Altura: '))
  peso = float(input('Peso: '))

  if clientes == 0:
    maisAlto = altura
    maisBaixo = altura
    maisGordo = peso
    maisMagro = peso
    maisAltoCodigo = codigo
    maisAltoCodigo = codigo
    maisBaixoCodigo = codigo
    maisMagroCodigo = codigo

  if altura > maisAlto:
    maisAlto = altura
    maisAltoCodigo = codigo

  if altura < maisBaixo:
    maisBaixo = altura
    maisBaixoCodigo = codigo

  if peso > maisGordo:
    maisGordo = peso
    maisGordoCodigo = codigo

  if peso < maisMagro:
    maisMagro = peso
    maisMagroCodigo = codigo
  
  clientes += 1

print('Mais gordo:', maisGordoCodigo, '-', maisGordo)
print('Mais magro:', maisMagroCodigo, '-', maisMagro)
print('Mais alto:', maisAltoCodigo, '-', maisAlto)
print('Mais baixo:', maisBaixoCodigo, '-', maisBaixo)
