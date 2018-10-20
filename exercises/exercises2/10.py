print('Qual turno você estuda?')
print('M-matutino ou V-Vespertino ou N-Noturno')

turno = input()
turno = turno.lower()

if turno == 'm' or turno == 'matutino':
  print('Bom dia')
elif turno == 'v' or turno == 'vespertino':
  print('Boa tarde')
elif turno == 'n' or turno == 'noturno':
  print('Boa noite')
else:
  print('Valor inválido')