def fib(n):
  "Fibonnaci until n"
  a, b = 0, 1
  while a < n:
    print(a)
    # a, b = b, a + b
    c = a + b
    a = b
    b = c
fib(10)

def fib2(n):
  "Returns Fibonnaci list"
  a, b = 0, 1
  numbers = []
  while a < n:
    numbers.append(a)
    a, b = b, a + b
  return numbers

def getFullname(*args):
  pass
  return args[0] + ' ' + args[1]

def hi(name, lastname):
  "Prints fullname"
  fullname = getFullname(name, lastname)
  print(fullname)

hi('alexandre', 'silva')

fibNumbers = fib2(10)
print(fibNumbers)

def confirm(question, attempts = 4, hint = '<Yes> or <No>'):
  "Confirms an action"
  while True:
    ok = input(question).lower()
    if ok in ('y', 'yes'):
      return True
    if ok in ('n', 'no'):
      return False
    attempts = attempts - 1
    if attempts == 0:
      raise IOError('User does not know what to do...')
    print(hint)

toDelete = confirm('Are you sure you want to DELETE this? ')
print('User:', toDelete)

print('----')

def allowProducts(product, qtt = 3, price = 10.4, **info):
  print('+----')
  print('You can buy', product, qtt, 'times, with a price of', price, 'each')
  print(product, 'info:')
  for key in info.keys():
    print('->', key, ':', info[key])

print('----')

allowProducts('CD')
allowProducts('DVD')
allowProducts('TV', price = 449)
allowProducts('Phone', price = 129, qtt = 1)
allowProducts('Smart TV', price = 129, qtt = 1, inch = 32)
# allowProducts('Phone', qtt = 1, price = 129, model = 3) # Parâmetro invalido, pois é desconhecido, a menos que haja um parâmetro **keywords

def multipleItems(item, *args):
  print(item, args)

multipleItems('item 1', 'legal')
multipleItems('item 2', 1, 2, 3, 4)
multipleItems('item 2', {1: True})

def sumNumber(number):
  "Sum a number to another"
  return lambda x: number + x

sum10 = sumNumber(10)

print(sum10(5))
print(sum10(7))


print(sumNumber.__doc__)