import random

def embaralha(palavra):
  return ''.join(random.sample(palavra, len(palavra)))

palavra = 'a'

while palavra != '':
  palavra = input('Palavra: ').lower()
  if palavra == '':
    exit()

  print(embaralha(palavra))