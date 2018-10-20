print('Valida e corrige número de telefone')
telefone = input('Telefone: ')

telefone = telefone.replace('-', '')

if len(telefone) == 7:
  print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
  telefone = '3' + telefone

telefoneFormatado = telefone[:4] + '-' + telefone[4:]


print('Telefone corrigido sem formatação:', telefone)
print('Telefone corrigido com formatação:', telefoneFormatado)
