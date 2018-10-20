populacaoA = -1
populacaoB = -1
crescimentoA = -1
crescimentoB = -1

while True:
  while populacaoA <= 0:
    populacaoA = input('População A: ')
    try:
      populacaoA = int(populacaoA)
    except:
      populacaoA = 0

  while crescimentoA <= -1 or crescimentoA > 100:
    crescimentoA = input('Taxa de crescimento da cidade A: ')
    try:
      crescimentoA = float(crescimentoA)
      crescimentoA = crescimentoA / 100
      crescimentoA += 1
    except:
      crescimentoA = -1

  while populacaoB <= 0:
    populacaoB = input('População B: ')
    try:
      populacaoB = int(populacaoB)
    except:
      populacaoB = 0

  while crescimentoB <= -1 or crescimentoB > 100:
    crescimentoB = input('Taxa de crescimento da cidade B: ')
    try:
      crescimentoB = float(crescimentoB)
      crescimentoB = crescimentoB / 100
      crescimentoB += 1
    except:
      crescimentoB = -1

  anos = 0

  maior = populacaoA
  menor = populacaoB
  crescimentoMaior = crescimentoA
  crescimentoMenor = crescimentoB
  if populacaoB >= populacaoA:
    maior = populacaoB
    menor = populacaoA
    crescimentoMaior = crescimentoB
    crescimentoMenor = crescimentoA

  while menor <= maior:
    menor = menor * crescimentoMenor
    maior = maior * crescimentoMaior
    anos += 1

  print('Levará', anos, 'anos')

  populacaoA = -1
  populacaoB = -1
  crescimentoA = -1
  crescimentoB = -1
