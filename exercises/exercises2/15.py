lado1 = float(input('Insira o 1º lado do triângulo: '))
lado2 = float(input('Insira o 2º lado do triângulo: '))
lado3 = float(input('Insira o 3º lado do triângulo: '))

triangulo = True

if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
  print('Os valores formam um triângulo')
else:
  triangulo = False
  print('Os valores não formam um triângulo')

if not triangulo:
  exit()

if lado1 == lado2 and lado1 == lado3:
  print('Triângulo Equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print('Triângulo Isoceles')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
  print('Triângulo Escaleno')
