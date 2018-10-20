while True:
  n = -1

  while n < 0 or n > 16:
    n = int(input('Informe um número: '))
  resultado = 1

  while n > 1:
    resultado *= n
    n -= 1

  print(resultado)

  n = -1