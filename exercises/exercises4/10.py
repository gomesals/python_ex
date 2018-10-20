vetor1 = []
vetor2 = []
vetor3 = []

while len(vetor1) < 10:
  vetor1.append(int(input('Vetor 1: ')))

while len(vetor2) < 10:
  vetor2.append(int(input('Vetor 2: ')))

for i in range(10):
  vetor3.append(vetor1[i])
  vetor3.append(vetor2[i])

print(vetor3)