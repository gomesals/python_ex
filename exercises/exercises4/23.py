# file = open('usuarios.txt', 'r')


espacoTotal = 0

usuarios = []
espacos = []

with open('usuarios.txt', 'r') as file:
  for line in file:
    nome = line[:15].strip()
    espaco = int(line[15:].strip())
    usuarios.append(nome)
    espacos.append(espaco)
    espacoTotal += espaco

print('ACME Inc.               Uso do espaço em disco pelos usuários')
print('------------------------------------------------------------------------')
print('Nr.  Usuário        Espaço utilizado     % do uso')
print('')


def to_mb(valor):
  'Retorna o valor em MB'
  return round(valor / 1024 / 1024, 2)

def get_porcento(valor, total):
  'Retorna a porcentagem do valor em relação a total'
  return round((valor * 100) / total, 2)

for i, nome in enumerate(usuarios):
  espaco = espacos[i]
  # porcentagem = round((espaco * 100) / espacoTotal, 2)
  print(str(i + 1).ljust(4), nome.ljust(14), str(to_mb(espaco)).rjust(13), 'MB', str(get_porcento(espaco, espacoTotal)).rjust(10), '%')

media = round(espacoTotal / len(usuarios), 2)
print('Espaço total ocupado:', to_mb(espacoTotal), 'MB')
print('Espaço médio ocupado', to_mb(media), 'MB')