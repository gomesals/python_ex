nome = ''
idade = -1
salario = -1
sexo = 'n'
civil = 'n'


while len(nome) <= 3:
  nome = input('Informe o nome: ')

while idade < 0 or idade > 150:
  idade = input('Informe a idade: ')
  try:
    idade = int(idade)
  except:
    idade = -1

while salario < 0:
  try:
    salario = float(input('Informe o salário: '))
  except:
    salario = -1

while sexo != 'f' and sexo != 'm':
  sexo = input('Informe o sexo, F-Feminino, M-Masculino: ').lower()

while civil != 's' and civil != 'c' and civil != 'v' and civil != 'd':
  civil = input('Informe o estado civil C-Casado, S-Solteiro, V-Viúvo, D-Divorciado: ').lower()