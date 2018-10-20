def validaCpf(cpf):
  cpf = str(cpf)
  if (len(cpf) != 11 or cpf == '0'
   or cpf == '1'*11 or cpf == '2'*11
   or cpf == '3'*11 or cpf == '4'*11
   or cpf == '5'*11 or cpf == '6'*11
   or cpf == '7'*11 or cpf == '8'*11
   or cpf == '9'*11):
    return False

  add = 0
  for i in range(9): add += int(cpf[i]) * (10 - i)
  rev = 11 - (add % 11)
  if rev == 10 or rev == 11: rev = 0
  if rev != int(cpf[9]): return False

  add = 0
  for i in range(10): add += int(cpf[i]) * (11 - i)
  rev = 11 - (add % 11)
  if rev == 10 or rev == 11: rev = 0
  if rev != int(cpf[10]): return False

  return True

cpf = ''

while True:
  cpf = input('CPF(xxx.xxx.xxx.xxx-xx): ')
  cpf = cpf.replace('.', '').replace('-', '')
  if validaCpf(cpf):
    print('CPF Válido')
  else:
    print('CPF Inválido')
