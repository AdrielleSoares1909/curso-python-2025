# Funcao PAR OU IMPAR

def par_impar(numero:int):
    if numero % 2 == 0:
        print("Esse numero é par.")
    else:
        print("Esse numero é impar.")

numero = input("Digite um numero : ")
numero = int(numero)

par_impar(numero)


