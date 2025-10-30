# DICIONARIO  = { CHAVE + VALOR }


dados_drica = {"nome": "drica", 
               "filhos" : "True",
               "sobrenome" : "Soares",
               "formacao" : ["Analise e desenvolvimento de Sistemas", 
                             "Curso Teo Calvo"],
                "cargos" : [
                    {"nome" : "atendente jr", "empresa" : "Algar telecom"},
                    {"nome" : "atendente ativo", "empresa" : "Martins Atacadista"},
                    {"nome" : "atendente cobrança", "empresa" : "NW Administradora"},
                ]
}
''' 
print(dados_drica) # dicionario { }

print(dados_drica["nome"]) # acessar chave nome 

print(dados_drica["formacao"][-1]) # pega sempre o ultimo -- acessa a lista de formacao [ ]
print(dados_drica["formacao"]) # acessa todos da lista da formacao

print(dados_drica["cargos"][1]) # acessa a lista de  cargos dentro do dicionario

print(dados_drica["cargos"][1]["empresa"]) # acessa a lista de cargos, o idice 1 e o nome da empresa dentro da lista no dicionario.

dados_drica["estado civil"] = "casada"  # Criar nova chave no dicionario 


'''
print(dados_drica)

print(dados_drica.keys()) # keys saber quais sao as chaves do meu dicionario
 
print(dados_drica.values()) # values saber quais sao os valores do meu dicionario 

print(dados_drica.items()) # items é uma lista de TUPLAS, que tem a chave na primeira posicao e o valor na segunda posicao

# exemplo de for 

for i in dados_drica: # percorre a lista mostrando as chaves 
    print(i, "->", dados_drica[i]) # percorre a lista mostra as chaves e tbm os valores 

# outro exemplo para percorrer o dicionario utilizando for 

for chave,valor in dados_drica.items():
    print(chave, "->", valor)