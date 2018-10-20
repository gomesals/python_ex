validValue = False

while not validValue:
  nota = input('Insira uma nota de 0 a 10: ')
  try:
    nota = int(nota)
    if nota >= 0 and nota <= 10:
      validValue = True
    else:
      validValue = False
  except:
    validValue = False