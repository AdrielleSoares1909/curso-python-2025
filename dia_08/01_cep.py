# %%

import requests # para realizar requisicoes na web
import json # para tratar json de listas/dicionarios para arquivos
from tqdm import tqdm

import pandas as pd

# pegando varios ceps
ceps = [
    "38408000",
    "38407381",
    "38407385",
    "38407386",
    "38407387",
    "38407388",

]

url = "https://viacep.com.br/ws/{cep}/json/" # definimos a url base
dados = [] # colocar os ceps na lista

for i in tqdm(ceps): # navenga em todos os ceps
    resposta = requests.get(url.format(cep=i)) #  obter a resposta da request
    if resposta.status_code == 200: # verifica se o status code foi 200 sucesso
        dados.append(resposta.json()) # adiciona a resposta em json 


dados
# %%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %%
with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

