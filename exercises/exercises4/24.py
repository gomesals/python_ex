import random

def lanca_dados():
  'Retorna um número aleatório entre 1 e 6'
  return random.randint(1, 6)

valores = [0,0,0,0,0,0]

resultados = []

while len(resultados) < 100:
  valor = lanca_dados()
  resultados.append(valor)
  valores[valor - 1] += 1

for i, v in enumerate(valores):
  print(i + 1, ':', v)