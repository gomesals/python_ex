frase = input('Palavra: ').lower()

def leet_translator(frase):
  frase = frase.replace('a', '4')
  frase = frase.replace('b', '8')
  frase = frase.replace('e', '3')
  frase = frase.replace('g', '9')
  frase = frase.replace('i', '1')
  frase = frase.replace('o', '0')
  frase = frase.replace('s', '5')
  frase = frase.replace('t', '7')
  frase = frase.replace('z', '2')
  return frase

print(leet_translator(frase))