palavra = input('Palavra: ')

def inverte(texto):
  inverso = ''
  for n in range(0, len(texto)):
    inicio = len(texto) - 1 - n
    fim = len(texto) - n
    inverso += texto[inicio:fim]
  return inverso

def isPalindromo(palavra):
  palavra = palavra.replace(' ', '')
  if len(palavra) % 2 == 0:
    metade = len(palavra) / 2
    metade = int(metade)
    segundaMetade = palavra[metade:len(palavra)]
  else:
    metade = (len(palavra) - 1) / 2
    metade = int(metade)
    segundaMetade = palavra[metade+1:len(palavra)]


  primeiraMetade = palavra[0:metade]

  segundaMetade = inverte(segundaMetade)

  return segundaMetade == primeiraMetade

if isPalindromo(palavra):
  print('Palíndromo')
else:
  print('Não é palíndromo')