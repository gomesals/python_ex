import math

tamanho = float(input('Qual o tamanho do arquivo (em MB)? '))
velocidade = int(input('Qual a velocidade da sua internet (em Mbps)? '))

tamanho = tamanho * 8 # Em megabit (mb)
tempo = tamanho / velocidade / 60

print('--')
if tempo < 1:
  tempo = tempo * 60
  print(tempo, 'segundo(s)')
else:
  tempo = math.ceil(tempo)
  print(tempo, 'minutos')
