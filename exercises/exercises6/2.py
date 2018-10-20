def inverte(texto):
  inverso = ''
  for n in range(0, len(texto)):
    inicio = len(texto) - 1 - n
    fim = len(texto) - n
    inverso += texto[inicio:fim]
  return inverso

nome = input('Nome: ').upper()

print(inverte(nome))