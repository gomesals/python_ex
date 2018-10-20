INICIO = 1995
FINAL = 2018


salario = float(input('Informe o salário: '))

ano = INICIO + 1
aumento = 0.015

while ano <= FINAL:
  salario = salario * (aumento + 1)
  # print(ano, '+', aumento, '%')
  aumento *= 2
  ano += 1

salario = round(salario, 2)

# print('aumento', aumento)

print('Salario para', FINAL, ': R$', salario)