"""
Considere a lista: [120, “Python”, 120.01, “asw”, False, [10,20] 

Faça um programa que retorne as seguintes informações:
Elemento na posição -1 da lista
Elemento na primeira posição da lista
O último caractere do segundo elemento da lista

Elemento -1: x
Primeiro elemento: y
Último caractere do segundo elemento: z

"""

lista = [120, "Python", 120.01, "asw", False, [10,20]]

print(lista)

print("Elemento -1 é : " , lista[-1])

print("Primeiro Elemento  é : " , lista[0])

print("Ultimo caractere do segundo elemento da minha lista é : " , lista[1][-1])