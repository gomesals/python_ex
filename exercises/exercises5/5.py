def somaImposto(taxaImposto, custo):
  imposto = taxaImposto / 100
  imposto = 1 + imposto
  return round(custo * imposto, 2)


print(somaImposto(10, 100))
print(somaImposto(3, 100))
print(somaImposto(25, 100))
print(somaImposto(1.5, 100))