x = int(input('Enter a number: '))

if x > 0:
  print(x, 'is bigger than 0')
elif x < 0:
  print(x, 'is lower than 0')
else:
  print(x, 'is equal to 0')


print('----')

list = ['cat', 'dog', 'bird']

for animal in list:
  print(animal, len(animal))

print('----')

for index in range(5):
  print(index)

print('----')

for index in range(5, 10):
  print(index)

print('----')

for index in range(5, 10, 2):
  print(index)

print('----')

for index in range(len(list)):
  print(index, list[index])

print('----')

limit = len(list)
i = 0
while i < limit:
  print(i, list[i])
  i = i + 1
