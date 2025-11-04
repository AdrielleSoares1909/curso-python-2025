# Calcular Imposto **KWARGS 

# **KWARGS = SERIA UM DICIONARIO = ADICIONA PARAMETROS NOMEADOS DE FORMA INDEFINIDA,QTDA INDEFINIDA,TAMANHO INDEFINIDO DENTRO DA FUNÇÃO.


def calc_imposto(preco:float, tx_base:0.03, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto


# criando um dicionario
impostos_gerias = {
    "municipio": 0.01,
    "estadual": 0.005,
    "nacional": 0.0001
}

print(calc_imposto(100,0.03, **impostos_gerias, internacional = 0.000001)) #exemplo 01

print(calc_imposto(100,0.03,municipio=0.01, estadual=0.005,nacional=0.0001)) # exemplo 02