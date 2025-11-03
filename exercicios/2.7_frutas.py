""" 
     EXERCICIO
    Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

        Maçã: R$1,50

        Banana: R$2,75

        Uva: R$1,90

        Pera: R$1,25

        Laranja: R$0,65

        Limão: R$1,25


        Goiaba: R$2,15

        Abacaxi: R$3,20

        Jaca: R$5,80

"""

lista_frutas = {"Maçã": "R$1,50",
                "Banana" : "R$2,75",
                "Uva" : "R$1,90",
                "Pera" : "R$1,25",
                "Laranja" : "R$0,65",
                "Limão" : "R$1,25",
                "Goiaba" : "R$2,15",
                "Abacaxi" : "R$3,20",
                "Jaca" : "R$5,80", }



fruta_escolhida = input("Selecione uma fruta da lista : ")

if fruta_escolhida in lista_frutas:
    print(lista_frutas[fruta_escolhida])
else:
    print("Entre com um valor valido!")