n = int(input('Informe um número maior que zero: '))

resultado = 1

while n > 1:
  resultado *= n
  n -= 1

print(resultado)