import random

def random_word(afile):
  line = next(afile)
  for num, aline in enumerate(afile):
    if random.randrange(num + 2):
      continue
    line = aline
  return line

with open('palavras.txt', 'r') as file:
  palavra = random_word(file).upper()

palavra = palavra.replace('\n', '')

erros = 0
acertou = False

palavraRevelada = []

for i in enumerate(palavra):
  palavraRevelada.append('_')

def revela_palavra(letra, palavra):
  indexes = []
  for index, l in enumerate(palavra):
    if l == letra:
      indexes.append(index)
  return indexes

def mostra_letraReservada(indexes):
  for i in indexes:
    palavraRevelada[i] = palavra[i]

def falta_adivinhar():
  acertou = 0
  for i in palavraRevelada:
    if i == '_':
      acertou += 1
  return acertou

def get_palavraReservada():
  palavra = ''
  for letra in palavraRevelada:
    palavra += letra + ' '
  return palavra

while erros < 6 and not acertou:
  letra = input('Digite uma letra: ').upper()
  if letra not in palavra:
    erros += 1
    print('Você errou pela', erros, 'ª vez. Tente de novo!')
    print('')
    continue

  indexes = revela_palavra(letra, palavra)
  mostra_letraReservada(indexes)

  print('A palavra é:', get_palavraReservada())
  print('')

  if falta_adivinhar() == 0:
    print('Venceu!')
    acertou = True