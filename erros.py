
while True:
  try:
    x = int(input('Número inteiro: '))
  except KeyboardInterrupt:
    print('\nQuer sair né? Tá bom...')
    exit()
  except ValueError as err:
    print('Isso aí não é um número inteiro hein!')
    print('-->', err)
  except:
    print('Opa, algo aconteceu e não sei o que foi.')
  else:
    print('Tudo ok')
  finally:
    print('Não importa o que houve, já passou...')

  try:
    raise NameError('pera ai amigo..')
  except NameError:
    print('Opaaa')
    # raise

  try: 
    'a' + 3
  except TypeError:
    print('Não consegui somar...')