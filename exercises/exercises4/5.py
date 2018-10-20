n = []
PAR = []
IMPAR = []

while len(n) < 20:
  numero = int(input('Número: '))
  n.append(numero)
  if numero % 2 == 0:
    PAR.append(numero)
  else:
    IMPAR.append(numero)

print(n)
print(PAR)
print(IMPAR)