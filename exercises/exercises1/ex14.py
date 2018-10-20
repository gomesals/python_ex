PESO_MAX = 50.00
MULTA = 4.05

peso = float(input('Quantos quilos de peixe você pegou hoje? '))
excesso = peso - PESO_MAX
multa = excesso * MULTA

if excesso > 0:
  print('Você pegou', excesso, 'Kg a mais que o permitido')
  print('Sua multa é de:', 'R$', multa)
else :
  print('Você não pegou peso excedente, por isso está livre de multa')