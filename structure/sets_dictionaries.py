# Sem elementos duplicados

frutas = set(('banana', 'laranja', 'uva'))
print(frutas)

frutas = {'banana', 'laranja', 'pera', 'uva'}
print(frutas)

emptySet = set()
dictionary = {}

print('banana' in frutas)
print('morango' in frutas)

print('')

a = set('alexandre')
b = set('silva')
print(a) # Letras únicas
print(a - b) # Letras em a, mas não em b
print(b - a) # Letras em b, mas não em a
print(a | b) # Letras em a ou b
print(a & b) # Letras em a e b
print(a ^ b) # Letras em a ou b, mas não em ambos

print('----')

numeros = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco'}
print(numeros)
print(list(numeros.keys()))

numeros = {'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5}
print(numeros)
# print(sorted(list(numeros.keys())))

numeros = dict([('um', 1), ('dois', 2), ('tres', 3)])
print(numeros)

numeros = dict(um=1, dois=2, tres=3)
print(numeros)

print(list(numeros.keys()))
print(sorted(numeros.keys()))
print(list(numeros.values()))

for key, value in numeros.items():
  print(key, ':', value)