frase = input('Frase: ')

print('Espaços:', frase.count(' '))

vogalA = frase.count('a')
vogalE = frase.count('e')
vogalI = frase.count('i')
vogalO = frase.count('o')
vogalU = frase.count('ou')

vogais = vogalA + vogalE + vogalI + vogalO + vogalU

print('Vogais:', vogais)