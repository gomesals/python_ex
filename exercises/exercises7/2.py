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


def to_mb(valor):
  'Retorna o valor em MB'
  return round(valor / 1024 / 1024, 2)

def get_porcento(valor, total):
  'Retorna a porcentagem do valor em relação a total'
  return round((valor * 100) / total, 2)


with open('relatório.txt', 'w') as file:
  file.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
  file.write('------------------------------------------------------------------------\n')
  file.write('Nr.  Usuário        Espaço utilizado     % do uso\n\n')

  for i, nome in enumerate(usuarios):
    espaco = espacos[i]
    linha = str(i + 1).ljust(5) + nome.ljust(14) + str(to_mb(espaco)).rjust(14) + ' MB' + str(get_porcento(espaco, espacoTotal)).rjust(12) + '%\n'
    file.write(linha)

  file.write('\n')
  media = round(espacoTotal / len(usuarios), 2)
  file.write('Espaço total ocupado: ' + str(to_mb(espacoTotal)) + ' MB\n')
  file.write('Espaço médio ocupado ' + str(to_mb(media)) + ' MB\n')