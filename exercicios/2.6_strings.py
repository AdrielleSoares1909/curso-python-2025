'''
    Escreva um programa que solicite ao usuário duas strings 
    e as 
    concatene em uma única String. Em seguida, exiba a String resultante.
'''

nome = input("Digite o seu nome: ")

sobrenome = input("Digite o seu sobrenome : ")

nome_completo = (nome + sobrenome)

print("Seu nome ", nome, " + seu sobrenome ", sobrenome, "é : ", nome_completo)