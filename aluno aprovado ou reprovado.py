nota1 = float (input("digite a primeira nota do aluno"))
nota2 = float (input("digite a segunda nota do aluno"))
nota3 = float (input("digite a terceira nota do aluno"))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f"O aluno esta aprovado com media {media:.2f}")
if media <4:
    print(f"O aluno está reprovado com a média de: {media:.2f}")
if media >=4 <7:
    print("você está de recuperação!!")
