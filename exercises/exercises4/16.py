salarios = []

tabela = [0,0,0,0,0,0,0,0,0]
intervalos = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699], [700, 799], [800, 899], [900, 999], [1000]]

atual = -1

def get_tabela_index(salario):
  for index, alcance in enumerate(intervalos):
    if len(alcance) == 1:
      if salario >= alcance[0]:
        return index
    if salario >= alcance[0] and salario <= alcance[1]:
      return index


while atual != 0:
  atual = int(input('Vendas: '))
  if atual == 0:
    break
  comissao = atual * 0.09
  salario = 200 + comissao
  salarios.append(salario)
  index = get_tabela_index(salario)
  tabela[index] += 1

for index, alcance in enumerate(intervalos):
  if len(alcance) == 1:
    print('>=', alcance[0], '==>', tabela[index])
    continue
  print('>=', alcance[0], '& <', alcance[1], '==>', tabela[index])