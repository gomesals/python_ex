altura = float(input('Insira sua altura (em metros): '))

pesoIdealHomem = 72.7 * altura - 58
pesoIdealMulher = 62.1 * altura - 44.7

pesoIdealHomem = round(pesoIdealHomem, 2)
pesoIdealMulher = round(pesoIdealMulher, 2)

print('Se você for homem, seu peso ideal é de:', pesoIdealHomem, 'Kg')
print('Se você for mulher, seu peso ideal é de:', pesoIdealMulher, 'Kg')