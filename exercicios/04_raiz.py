numero = input("Digite um numero inteiro para calcular sua raiz quadrada: ")


numero = int(numero)

raiz = numero ** (1/2)  # ou numero ** 0.5
raiz = round(raiz, 4)

print("Raiz quadrada de ", numero, "é:" , raiz)