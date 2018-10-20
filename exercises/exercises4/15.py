valores = []
valor = 0

media = 0
soma = 0

while valor != -1:
  valor = int(input('Número: '))
  if valor == -1:
    break

  media += valor

  valores.append(valor)

soma = media
media = round(media / len(valores), 2)

print('Valores lidos:', len(valores))

for i in valores:
  print(i, end=" ")
print('')

inverso = valores.copy()
inverso.reverse()

for i in inverso:
  print(i, end=" ")
print('')

acimaDaMedia = [x for x in valores if x > media]
print('Acima da media:', acimaDaMedia)

abaixoDe7 = [x for x in valores if x < 7]
print('Abaixo de 7:', abaixoDe7)

print('Fim')