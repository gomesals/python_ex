import itertools

def mesma_soma(v):
  valores = [int(x) for x in v]
  soma1 = valores[0] + valores[1] + valores[2]
  soma2 = valores[3] + valores[4] + valores[5]
  soma3 = valores[6] + valores[7] + valores[8]
  soma4 = valores[0] + valores[3] + valores[6]
  soma5 = valores[1] + valores[4] + valores[7]
  soma6 = valores[2] + valores[5] + valores[8]
  soma7 = valores[0] + valores[4] + valores[8]
  soma8 = valores[6] + valores[4] + valores[2]

  if soma1 != soma2:
    return False
  if soma1 != soma3:
    return False
  if soma1 != soma4:
    return False
  if soma1 != soma5:
    return False
  if soma1 != soma6:
    return False
  if soma1 != soma7:
    return False
  if soma1 != soma8:
    return False
  return True

def imprime(valores):
  print(valores[0], valores[1], valores[2])
  print(valores[3], valores[4], valores[5])
  print(valores[6], valores[7], valores[8])

valores = list(itertools.permutations('123456789', 9))

for valor in valores:
  if mesma_soma(valor):
    imprime(valor)
    print('')
