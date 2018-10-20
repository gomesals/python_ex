# numero = int(input('Insira um número inteiro: '))

numero = 326

def reverse_str(string):
  return string
  return string[::-1]

if numero >= 1000:
  print('Número maior que mil')
  exit()

numeroString = reverse_str(str(numero))

quantidade = ''

for index, num in enumerate(numeroString):
  number = int(num)
  if index == 0 and number > 0:
    quantidade += num + ' unidade'
  if index == 1 and number > 0:
    quantidade += num + ' dezena'
  if index == 2 and number > 0:
    quantidade += '' + num + 'centena'

  if number > 1:
    quantidade += 's'

  # if 
  # print(index, 'ii')
  # print(numeroString[index])

print(quantidade)
# numeros = str(numero).split()

# print(numeros)