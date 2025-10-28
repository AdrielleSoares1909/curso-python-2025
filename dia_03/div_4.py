#um numero divisivel por 4 o resto tem que ser 0


# Quais numeros sao divisiveis por 4 no intervalo [4 - 100]?
# usar i ou count

count = 4

while count <= 100:
    resto = count % 4
    if resto == 0 :
        print(count)
    
    count += 1
