import random


def embaralha(palavra):
  return ''.join(random.sample(palavra, len(palavra)))

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

embaralhada = embaralha(palavra)
 
print(embaralhada)

while erros < 6 and not acertou:
  tentativa = input('Palavra: ').upper()

  if palavra == tentativa:
    print('Venceu!!')
    exit()
  else:
    erros += 1
    print('Você errou pela', erros, 'ª vez. Tente de novo!')
    print('')
    continue
