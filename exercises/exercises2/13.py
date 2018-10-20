dia = int(input('Digite um número inteiro: '))

def dia_semana(dia):
  semana = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sábado'
  }
  return semana.get(dia, 'Valor inválido')

diaSemana = dia_semana(dia)
print(diaSemana)