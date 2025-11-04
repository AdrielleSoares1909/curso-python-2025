
# Juros Compostos - FUNÇÃO


def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros_compostos serve para calcular o retorno financeiro a partir 
    de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos)
    para calculo do valor a ser retornado.

    Args:
        aporte (int): um numero inteiro,que represente o valor em R$
        taxa (float): um numero float entre 0 e 1 que represente o valor da taxa de juros atual
        anos (int): um numero inteiro >= 1 que representa o tempo que o investimento tera liquidez

    Returns:
        float: resultado final do calculo
    """
    return aporte * (1 + taxa) ** anos


print(juros_compostos(aporte=1000, taxa=0.13, anos=4))

print(juros_compostos(aporte=1000, taxa=0.10, anos=10))

