perguntas = {
  0: "Telefonou para a vítima?",
  1: "Esteve no local do crime?",
  2: "Mora perto da vítima?",
  3: "Devia para a vítima?",
  4: "Já trabalhou com a vítima?" 
}

situacao = {
  0: 'Inocente',
  1: 'Inocente',
  2: 'Suspeita',
  3: 'Cúmplice',
  4: 'Cúmplice',
  5: 'Assassino'
}

respostas = []
soma = 0

while len(respostas) < len(perguntas):
  question = perguntas[len(respostas)] + ' S-Sim, N-Não: '
  resposta = input(question).lower()
  respostas.append(resposta)
  if resposta == 's' or resposta == 'sim':
    soma += 1

print('Situação:', situacao[soma])