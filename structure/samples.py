pergunta = ['altura', 'idade', 'cor favorita']
resposta = [175, 24, 'azul']

for p, r in zip(pergunta, resposta):
  print('Qual a sua {0}? Parece ser {1}'.format(p, r))

frutas = ['banana', 'maçã', 'pera', 'uva']

for fruta in sorted(set(frutas)):
  print(fruta)

