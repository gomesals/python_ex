tipoCarne = input('Qual o tipo da carne, F-Filé Duplo, A-Alcatra, P-Picanha ? ').lower()
peso = float(input('Quantos quilos da carne? '))
tipoPagamento = input('Como você irá pagar? C-Cartão Tabajara, D-Dinheiro: ').lower()


def preco_carne(carne, peso):
  if peso < 5:
    if carne == 'f':
      return peso * 4.9
    elif carne == 'f':
      return peso * 5.9
    else:
      return peso * 6.9
  else:
    if carne == 'f':
      return peso * 5.8
    elif carne == 'f':
      return peso * 6.8
    else:
      return peso * 7.8

if tipoCarne == 'f':
  carne = 'Filé Duplo'
elif tipoCarne == 'a':
  carne = 'Alcatra'
elif tipoCarne == 'p':
  carne = 'Picanha'
else:
  print('Carne inválida')
  exit()

preco = preco_carne(tipoCarne, peso)
preco = round(preco, 2)

desconto = 0
pagamento = 'Dinheiro'
if tipoPagamento == 'c':
  pagamento = 'Cartão Tabajara'
  desconto = 0.05

desconto = preco * desconto

pagar = preco - desconto

print(carne, ':', peso, 'Kg')
print('Preço total: R$', preco)
print('Tipo de pagamento: ', pagamento)
print('Valor do desconto: R$', desconto)
print('Valor a pagar: R$', pagar)