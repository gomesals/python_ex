base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))

quo = 1

resultado = base
while expoente > quo:
  resultado = resultado * base
  expoente -= 1

print(resultado)