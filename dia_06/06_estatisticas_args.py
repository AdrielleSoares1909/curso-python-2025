# funcao utilizando *ARGS

# *ARGS = PODE SER QUALQUER NOME, E ADICIONA ELEMENTOS.

def soma(a:float, b:float, *args)->float: 
    valores = [a,b] + list(args)
    return sum(valores) 


# funcao media usando dentro dela a funcao soma

def media(a:float, b:float, *args)->float:
    return soma (a,b, *args) / (len(args) + 2)  # reutilizando a funcao soma para calcular a media

a = float(input("entre com o valor a: "))
b = float(input("entre com o valor b: "))
c = float(input("entre com o valor c: "))
d = float(input("entre com o valor d: "))

print("soma: ", soma(a,b,c,d))
print("media: ", media(a,b,c,d))