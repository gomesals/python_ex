LITRO_GASOLINA = 2.5
LITRO_ALCOOL = 1.9

litros = int(input('Quantos litros de combustível? '))
tipo = input('Qual o tipo de combustível, A-álcool, G-gasolina? ').lower()



if litros <= 20:
  descontoGrande = False
else:
  descontoGrande = True

if tipo == 'a':
  if descontoGrande:
    desconto = 0.05
  else:
    desconto = 0.03
  desconto = 1 - desconto
  precoLitro = LITRO_ALCOOL * desconto
elif tipo == 'g':
  if descontoGrande:
    desconto = 0.06
  else:
    desconto = 0.04
  desconto = 1 - desconto
  precoLitro = LITRO_GASOLINA * desconto
else:
  print('Combustível inválido')
  exit()

valor = litros * precoLitro
total = round(valor, 2)

print('Valor a ser pago:', 'R$', total)
