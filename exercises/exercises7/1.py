validos = []
invalidos = []


def is_valid(numbers):
  for number in numbers:
    number = int(number)
    if number >= 256: return False
    if number == 0: return False
    if number == 5: return False
  return True


with open('ips.txt', 'r') as file:
  for line in file:
    line = line.replace('\n', '')
    numbers = line.split('.')
    if is_valid(numbers):
      validos.append(line)
    else:
      invalidos.append(line)


with open('_ips.txt', 'w') as file:
  file.write('[Endereços válidos:]\n')
  for i in validos:
    file.write(i + '\n')
  file.write('\n')
  file.write('[Endereços inválidos:]\n')
  for i in invalidos:
    file.write(i + '\n')
