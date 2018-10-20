import re


n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
operacao = input('Qual operação deseja realizar? (+ - * :) : ')

if operacao == '+':
  resultado = n1 + n2
elif operacao == '-':
  resultado = n1 - n2
elif operacao == '*':
  resultado = n1 * n2
elif operacao == ':':
  resultado = n1 / n2
else:
  print('Operação inválida')
  exit()

print('Resultado: ', resultado)

if resultado % 2 == 0:
  print('O resultado é par')
else:
  print('O resultado é ímpar')

if resultado >= 0:
  print('O resultado é positivo')
else:
  print('O resultado é negativo')

n = str(round(resultado, 2))

if re.search(".0$", n) is not None:
  print('O resultado é inteiro')
else:
  print('O resultado é decimal')
