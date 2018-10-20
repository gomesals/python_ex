import math

VALOR_LATA = 80.00
VALOR_GALAO = 25.00
METROS_POR_LITRO = 6

GALAO_MELHOR = math.floor(VALOR_LATA / VALOR_GALAO)
GALAO_MELHOR_METROS = math.floor(3.6 * 3 * 6)

area = float(input('Qual a quantidade de metros a ser pintada (em metros quadrados)? '))

# area = 120

litros = math.ceil(area / METROS_POR_LITRO)
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)

print(latas, 'latas', ' | Preço total:', 'R$', latas * VALOR_LATA)
print(galoes, 'galões', ' | Preço total:', 'R$', galoes * VALOR_GALAO)

area = area * 1.1
litros = math.ceil(area / 6)
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)


print()
print('# Melhor opção:')

if area < GALAO_MELHOR_METROS:
  print(galoes, 'galões de tinta', '| Preço total:', 'R$', galoes * VALOR_GALAO)
else: 
  if latas <= 1:
    print(latas, 'latas de tinta', '| Preço total:', 'R$', latas * VALOR_LATA)
  else:
    latas = latas - 1
    novaArea = area - 18 * latas * 6
    galoes = math.ceil(novaArea/ 6 / 3.6)
    if galoes <= 3:
      total_lata = latas * VALOR_LATA
      total_galao = galoes * VALOR_GALAO
      total = latas * VALOR_LATA + galoes * VALOR_GALAO
      print(latas, 'lata(s) e', galoes, 'galão(ões) de tinta:', 'R$', total_lata, '+', 'R$', total_galao, '=', 'R$', total)
    else:
      latas = latas + 1
      print(latas, 'latas de tinta', '| Preço total:', 'R$', latas * VALOR_LATA)
