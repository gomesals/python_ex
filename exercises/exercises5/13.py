def moldura(linhas, colunas):
  linhas += 2
  colunas += 2
  for linha in range(0, linhas):
    if linha == 0 or linha == linhas - 1:
      print('+', end="")
      for coluna in range(1, colunas):
        if coluna == colunas - 1:
          print('+', end="")
        else:
          print('-', end="")
    else:
      print('|', end="")
      for coluna in range(1, colunas):
        if coluna == colunas - 1:
          print('|', end="")
        else:
          print(' ', end="")
    print()
    # print()
  # print(linhas, colunas)

linha = 1
coluna = 1

while linha >= 1 and linha <= 20 and coluna >= 1 and coluna <= 20:
  linha = int(input('Linhas: '))
  coluna = int(input('Colunas: '))

  if linha <= 0 or linha > 20 or coluna <= 0 or coluna > 20:
    exit()

  moldura(linha, coluna)