print('Informe uma data no formato dd/mm/aaaa')
data = input()

def is_bi(ano):
  if ano % 4 == 0 and ano % 100 != 0:
    return True
  else:
    if ano % 400 == 0:
      return True
    else:
      return False

def finalizar():
  print('Data inváida')
  exit()

if len(data) != 10:
  finalizar()

data = data.split('/')

if len(data) != 3:
  finalizar()

if len(data[0]) != 2 and len(data[1]) != 2 and len(data[2]) != 4:
  finalizar()

dia, mes, ano = data

try:
  dia = int(dia)
  mes = int(mes)
  ano = int(ano)
except:
  finalizar()

if dia < 1 or dia > 31:
  finalizar()

if ano < 0:
  finalizar()

if mes == 2 and dia == 29:
  if not is_bi(ano):
    finalizar()

if dia == 31:
  if not (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    finalizar()

print('Data válida')
