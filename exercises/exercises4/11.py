vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

while len(vetor1) < 10:
  vetor1.append(int(input('Vetor 1: ')))

while len(vetor2) < 10:
  vetor2.append(int(input('Vetor 2: ')))

while len(vetor3) < 10:
  vetor2.append(int(input('Vetor 3: ')))

for i in range(10):
  vetor4.append(vetor1[i])
  vetor4.append(vetor2[i])
  vetor4.append(vetor3[i])

print(vetor4)