numero = input('Informe um número: ')

print('O valor é ', end = "")

try:
  int(numero)
  print('inteiro')
except:
  try:
    float(numero)
    print('decimal')
  except:
    print('string')
