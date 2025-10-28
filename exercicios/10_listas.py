lista = [1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5, 5, 5, 5, 5]

numero = input("Digite um numero: ")
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de", numero, ":", contador)