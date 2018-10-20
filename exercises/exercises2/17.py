ano = int(input('Informe um ano: '))

bissexto = 'não é bissexto'

if ano % 4 == 0 and ano % 100 != 0:
  bi = True
else:
  if ano % 400 == 0:
    bi = True
  else:
    bi = False

if bi:
  bissexto = 'é bissexto'

print('O ano', ano, bissexto)