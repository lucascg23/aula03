g = 5.80
e = 4.90
combu = (input("Escreva G se quiser colocar gasilina ou E se quiser etanol: "))

if combu == "g" or combu== "G" :
    gg= float (input("escreva a quantidade de litros desejado: "))
    litrosg=g * gg
    print(f"você vai pagar R$ {litrosg} de gasolina ")
else :
    if combu == "e" or combu == "E":
        ee = float(input("escreva a quantidade de litros desejado: "))
        litrose = e * ee
        print(f"você vai pagar R$ {litrose} de etanol ")
    else:
        print("tente novamente digitando G(g) ou E(e)")


