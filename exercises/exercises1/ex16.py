import math

VALOR_TINTA = 80.0

area = float(input('Qual a quantidade de metros a ser pintada (em metros quadrados)? '))

litros = math.ceil(area / 3)
latas = math.ceil(litros / 18)

print('Latas de tintas a serem compradas:', latas)
print('Preço total:', 'R$', latas * VALOR_TINTA)
