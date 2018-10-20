import random

def lanca_dados():
  'Retorna um número aleatório entre 1 e 6'
  return random.randint(1, 6)

def get_resultado(pontos):
  if pontos == 7 or pontos == 1:
    return 'natural'
  if pontos == 2 or pontos == 3 or pontos == 13:
    return 'craps'
  return 'ponto'

entrada = 1
ponto = 0
while entrada != '0':
  entrada = input('(0 para sair): ')
  if entrada == '0':
    exit()

  dado1 = lanca_dados()
  dado2 = lanca_dados()
  pontos = dado1 + dado2

  if ponto > 0:
    if pontos == ponto:
      resultado = 'ganhou'
      ponto = 0
    elif pontos == 7:
      resultado = 'perdeu'
    else:
      resultado = 'next'
  else:
    resultado = get_resultado(pontos)


  print('Dado 1:', dado1)
  print('Dado 2:', dado2)
  print('Soma:', pontos)

  if resultado != 'next':
    print(resultado)
  if resultado == 'ponto':
    ponto = pontos

  print('')