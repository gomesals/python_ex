formValid = False

while not formValid:
  usuario = input('Usuário: ')
  senha = input('Senha: ')
  if usuario == senha:
    print('Senha não pode ser igual ao usuário, tente novamente.')
    formValid = False
  else:
    formValid = True