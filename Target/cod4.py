sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

spPerc = (sp * 100) / total
rjPerc = (rj * 100) / total
mgPerc = (mg * 100) / total
esPerc = (es * 100) / total
outrosPerc = (outros * 100) / total


print(f"Segue os percentuais de representação que cada estado teve: ")
print(f"São Paulo = {spPerc:.2f}%")
print(f"Rio de Janeiro = {rjPerc:.2f}%")
print(f"Minas Gerais = {mgPerc:.2f}%")
print(f"Espirito Santo = {esPerc:.2f}%")
print(f"Outros = {outrosPerc:.2f}%")