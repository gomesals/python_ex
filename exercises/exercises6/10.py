numerosUnidade = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
numerosDecimal = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
numerosDecimalDez = ['onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

while True:
  numero = int(input('Número: '))

  if numero > 99 or numero < 0:
    continue

  numero = str(numero)
  if len(numero) == 1:
    print(numerosUnidade[int(numero[0])])
  else:
    if numero[1] == '0':
      print(numerosDecimal[int(numero[0]) - 1])
    elif numero[0] == '1':
      print(numerosDecimalDez[int(numero[0]) - 1])
    else:
      print(numerosDecimal[int(numero[0]) - 1], 'e', numerosUnidade[int(numero[1])])
