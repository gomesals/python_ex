salario = float(input('Informe o salário do funcionário: '))

aumento = 0.2

if salario > 280 and salario <= 700:
  aumento = 0.15
elif salario > 700 and salario <= 1500:
  aumento = 0.1
elif salario > 1500:
  aumento = 0.05

reajuste = round(salario * (aumento + 1), 2)

print('Salário (R$):', salario)
print('Aumento (%):', round(aumento * 100, 2))
print('Aumento (R$):', round(reajuste - salario, 2))
print('Novo salário (R$)', reajuste)