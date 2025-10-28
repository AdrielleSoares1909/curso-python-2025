
# Uma maneira de definir listas

idades = [28, 42, 43, 35, 28, 38, 34]
print(idades)

# exemplo 

drica = ["Adrielle", "Cristian", "34", True]

print(drica)

print(type(drica))

# exemplo 

# idade

print(drica[2])

# tem filhos

print(drica[3])

# exemplo

idades = [28, 42, 43, 35, 28, 38, 34, 55]

print("soma idades :" , sum(idades))

print("qtde idades:", len(idades))

print("media idades: ", sum(idades)/ len(idades))

print("menos idade: ", min(idades))

print("menor idade: ", max(idades))

# exemplo lista dentro de lista

drica = ["Adrielle Cristian", 34, True, "casada", ["Soares", "Pereira"], ["RAFAEL", "MIGUEL", "GABRIEL"]]

print(len(drica))

print(drica[5][0])

print(drica[5][1])

print(drica[4][0])

print(drica[2])

# exemplo
tamanho = len(drica) # tamanho da lista
pos = tamanho - 1 # ultima posicao
print(drica[pos])

# exemplo pegar o ultimo elemento da lista

print(drica[-1][-1])

print(drica[-1][-2])

print(drica[-1][0])

# FATIAMENTO

print(drica[0:4])

print(drica[5][0:3])

print(drica[4][0:2])

# drica[ start : stop : step] = exemplo 

# exemplo de mostrar na ordem inversa

nomes = drica[5]
print(nomes [::-1])