horas = int(input('Quantas horas trabalhou no mês? '))
valor = float(input('E qual o valor da sua hora de trabalho? '))

salario = horas * valor

ir = 0

if salario > 900 and salario <= 1500:
  ir = 0.05
elif salario > 1500 and salario <= 2500:
  ir = 0.1
elif salario > 2500:
  ir = 0.2

deducaoIr = salario * ir
# deducaoSindicato = salario * 0.03
deducaoInss = salario * 0.1
valorFgts = salario * 0.11

totalDesconto = deducaoInss + deducaoIr

print('Salário Bruto: (', valor, '*', horas, ')  :', 'R$', salario)
print('(-) IR (', ir * 100, '%)  :', 'R$', deducaoIr)
print('(-) INSS (10%)  :', 'R$', deducaoInss)
print('FGTS (11%)  :', 'R$', valorFgts)
print('Total de descontos:', 'R$', totalDesconto)
print('Salário Líquido:', 'R$', salario - totalDesconto)