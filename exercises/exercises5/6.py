def isAmOrPm(horas):
  if horas >= 12 and horas <= 23:
    return 'A'
  return 'P'

def converte_horas(horas, minutos):
  amPm = isAmOrPm(horas)
  if amPm == 'A':
    amPm = 'A.M.'
  else:
    amPm = 'P.M.'
  if horas > 12:
    horas -= 12

  horario = str(horas) + ':' + str(minutos) + ' ' + amPm
  return horario

hora = 'a'

while hora != '':
  hora = input('Hora (HH:mm): ')
  if hora == '':
    exit()

  try:
    horas, minutos = hora.split(':')
    horas = int(horas)
    minutos = int(minutos)
  except:
    continue
  if horas > 24 or horas < 0 or minutos > 59 or minutos < 0:
    continue

  print(converte_horas(horas, minutos))
