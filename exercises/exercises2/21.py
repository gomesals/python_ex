valor = int(input('Digite quanto deseja sacar: '))

if valor < 10 or valor > 600:
  print('Valor não permitido')
  exit()

notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0

while valor >= 100:
  notas100 += 1
  valor -= 100

while valor >= 50:
  notas50 += 1
  valor -= 50

while valor >= 10:
  notas10 += 1
  valor -= 10

while valor >= 5:
  notas5 += 1
  valor -= 5

while valor > 0:
  notas1 += 1
  valor -= 1

print('Notas de 100:', notas100)
print('Notas de 50:', notas50)
print('Notas de 10:', notas10)
print('Notas de 5:', notas5)
print('Notas de 1:', notas1)