def reverso(numero):
  numero = str(numero)
  numeroReverso = ''
  for i in range(0, len(numero)):
    inicio = len(numero) - 1 - i
    fim = len(numero) - i
    numeroReverso += numero[inicio:fim]
  return numeroReverso

print(reverso(100))
print(reverso(721))
print(reverso(1234))
print(reverso(300))