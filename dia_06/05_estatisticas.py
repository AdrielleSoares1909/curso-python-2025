# Funcao SOMA


def soma(a:float, b:float)->float: 
    return a + b 


# funcao media usando dentro dela a funcao soma

def media(a:float, b:float)->float:
    return soma (a,b) / 2  # reutilizando a funcao soma para calcular a media

a = float(input("entre com o valor a: "))
b = float(input("entre com o valor b: "))

print("soma: ", soma(a,b))
print("media: ", media(a,b))