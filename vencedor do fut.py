time1= input("insira o nome do time 1")

gols1= int (input(f"insira o numero de gols do {time1}"))

time2= input("insira o nome do time 2")

gols2= int (input(f"insira o numero de gols do {time2}"))

if gols1 > gols2:
    print(f"{time1} ganhou o jogo!")
else:
    if gols2>gols1:
        print(f"{time2} ganhou!!")
    else:
        print("o jogo empatou!!")