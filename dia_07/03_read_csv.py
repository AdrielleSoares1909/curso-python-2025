

arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)

dados = dict()

chaves = lines[0].strip("\n").split(";") 
for c in chaves:
    dados[c] = []

print(dados)

for l in lines[1:]:
    valores = l.strip("\n").split(";")
    dados[chaves[i]].append(valores[i])

idades = []
for i in dados["idades"]:
    idades.append(int(i))

print(idades)