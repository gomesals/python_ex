print(repr('1').ljust(5), '|')
print(repr('1').rjust(5), '|')

print('{0:5d}'.format(1), '|')

for i in range(1, 11):
  print(str(i).zfill(2))

print('Isto {objeto} é bem {adjetivo}'.format(objeto='aqui', adjetivo='interessante'))

nome = 'alexandre'
print('Meu nome é {}'.format(nome))
print('Meu nome é {!a}'.format(nome)) # ascii()
print('Meu nome é {!s}'.format(nome)) # str()
print('Meu nome é {!r}'.format(nome)) # repr()

valor = 10.124
print('Total: {0:.2f}'.format(valor))

reserva = {'NuConta': 13133, 'Caixa': 1231, 'Inter': 0}
for banco, valor in reserva.items():
  print('{0:15} ==>      R$ {1:8d}'.format(banco, valor))

print('NuConta: {NuConta:d}; Caixa: {Caixa:d}; Inter: {Inter:d}'.format(**reserva))