from collections import deque

list = [] # []

list.append(1) # [1]
list.append(2) # [1, 2]

list.extend([3, 4]) # [1, 2, 3, 4]

list.insert(5, 6) # [1, 2, 3, 4, 6]
list.insert(1, 5) # [1, 5, 2, 3, 4, 6]

list.remove(3) # [1, 5, 2, 4, 6]

try:
  list.remove(8)
except:
  print('Não tem o 8 na lista')

list.pop() # [1, 5, 2, 4] -> Retorna o 6
list.pop(1) # [1, 2, 4] -> Retorna o 5

list.index(4) # Retorna 3

list.count(1) # -> Retorna 1

list.sort() # [1, 2, 4]

list.reverse() # [4, 2, 1]

lista = list.copy() # [4, 2, 1]


list.clear() # []


del lista
del list

pilha = [1, 2, 3]
pilha.append(4) # [1,2,3,4]
pilha.append(5) # [1, 2, 3, 4, 5]
pilha.pop() # [1, 2, 3, 4]
pilha.pop() # [1, 2, 3]
pilha.pop() # [1, 2]

del pilha

fila = deque([1, 2, 3])
fila.append(4) # [1, 2, 3, 4]
fila.append(5) # [1, 2, 3, 4, 5]
fila.popleft() # [2, 3, 4, 5]
fila.popleft() # [3, 4, 5]

del fila

pares = [x for x in range(10) if x % 2 == 0]
print(pares)

quadrados = [x ** 2 for x in range(5)]
print(quadrados)

numeros_quadrados_cubos = [[x, x ** 2, x ** 3] for x in range(3)]
print(numeros_quadrados_cubos)

todos = [y for x in numeros_quadrados_cubos for y in x]
print(todos)

del todos[0]
del todos[0]
del todos[1]
del todos[1]

print(todos)

del quadrados
del numeros_quadrados_cubos
del todos

letras = ['a', 'b', 'c', 'd', 'e']
for index, letra in enumerate(letras):
  print(index + 1, '->', letra)
