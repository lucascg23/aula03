nome = (input("informe seu nome "))
idade = int (input("informe sua idade "))
salario = float (input("informe seu salário "))
porcentagem = float (input("quantos % o seu salario aumentou: "))
amais =  salario*porcentagem/100
nsalario = salario*porcentagem/100+salario
print(f"seu nome é {nome} você tem {idade}  anos e recebe um salário de R${salario:.2f} você agora vai receber um aumento de {amais:.2f}"
      f" e o seu novo salario vai ser de {nsalario:.2f}")

