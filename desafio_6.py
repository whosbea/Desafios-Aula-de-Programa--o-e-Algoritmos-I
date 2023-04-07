anoAtual = int(input("Qual o ano atual? "))
anoAniversario = int(input("Qual o seu ano de nascimento? "))
idade = anoAtual - anoAniversario

if idade < 16:
    print(f"Sua idade é {idade} anos e você ainda não pode votar")

else:
    print(f"Sua idade é {idade} anos e você ja pode votar")