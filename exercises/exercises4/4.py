n = []
con = []
while len(n) < 10:
  c = input('Informe um caractere: ')
  n.append(c)
  if not(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
    con.append(c)

for i in con:
  print(i)

print(len(con), ' consoantes')