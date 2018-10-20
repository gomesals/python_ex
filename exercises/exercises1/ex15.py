valor = float(input('Quanto você ganha por hora? '))
horas = int(input('Quantas horas você trabalhou? '))

salario = valor * horas

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

salarioLiquido = salario - ir - inss - sindicato

print('+', 'Salário Bruto :', 'R$', salario)
print('-', 'IR (11%) :', 'R$', ir)
print('-', 'INSS (8%) :', 'R$', inss)
print('-', 'Sindicato (5%) :', 'R$', sindicato)
print('=', 'Salário Líquido :', 'R$', salarioLiquido)
