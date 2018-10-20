n = int(input('Informe um número inteiro positivo: '))
numero = str(n)

numeroReverso = ''

for n in range(0, len(numero)):
  inicio = len(numero) - 1 - n
  fim = len(numero) - n
  numeroReverso += numero[inicio:fim]

print('=>', numeroReverso)