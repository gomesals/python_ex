total = 0
codigo = -1

listaDefeitos = ['necessita da esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector', 'quebrado ou inutilizado']

defeitos = [0,0,0,0]

while codigo != 0:
  codigo = int(input('Código: '))

  if codigo == 0:
    continue

  print('Defeitos:')
  for i, v in enumerate(listaDefeitos):
    print(i + 1, '-', v, end = '; ')
  print('')
  defeito = int(input('Tipo de defeito: '))

  defeitos[defeito - 1] += 1

  total += 1

print('')
print('Quantidade de mouses:', total)
print('{0:40} {1:10}          {2:10}'.format('Situação', 'Quantidade', 'Percentual'))

for i, v in enumerate(defeitos):
  porcentagem = round((v * 100) / total, 0)
  print(i + 1, '-', '{0:40}'.format(listaDefeitos[i]), '{0:6}'.format(v), ' '*8, '{0:8}'.format(porcentagem), '%')