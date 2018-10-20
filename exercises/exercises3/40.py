n = 0

veiculosMedia = 0
acidentesMedia = 0
acidentesMediaContador = 0

maior = 0
menor = 0
maiorC = ''
menorC = ''

while n < 5:
  codigo = input('Código da cidade: ')
  veiculos = int(input('Número de veículos de passeio (em 1999): '))
  acidentes = int(input('Número de acidentes de trânsito com vítimas (em 1999): '))

  if n == 0:
    menor = acidentes
    maior = acidentes
    maiorC = codigo
    menorC = codigo

  if acidentes > maior:
    maior = acidentes
    maiorC = codigo
  else:
    menor = acidentes
    menorC = codigo

  veiculosMedia += veiculos

  if veiculos < 2000:
    acidentesMedia += acidentes
    acidentesMediaContador += 1

  n += 1

print('Maior acidentes:', maiorC, '-', maior)
print('Menor acidentes:', menorC, '-', menor)
print('Média veículos:', veiculosMedia / 5)
print('Média de acidentes (para < 2000 veículos): ', round(acidentesMedia / acidentesMediaContador, 2))