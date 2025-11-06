# %%

txt = "Meu novo arquivo!"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="w") as open_file: # w = esccrever arquivo e o a = incluir novas informacoes no arquivo
    open_file.write(txt)
