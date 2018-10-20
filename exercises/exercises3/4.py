CRESCIMENTO_A = 1.03
CRESCIMENTO_B = 1.015

populacaoA = 80000
populacaoB = 200000

anos = 0

while populacaoA <= populacaoB:
  populacaoA = populacaoA * CRESCIMENTO_A
  populacaoB = populacaoB * CRESCIMENTO_B
  anos += 1

print('Levará', anos, 'anos')