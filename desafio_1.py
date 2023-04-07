import random


numeroEscolhido = int(input("Escreva um numero de 1 a 10 "))

numeroSecreto = random.randint(1, 10)

if numeroEscolhido > 10 or numeroEscolhido < 1:
    print("Escolha um numero entre 1 e 10")
if numeroEscolhido != numeroSecreto:
    print(f"Voce errou o numero era {numeroSecreto}")
else:
    print(f"Parabéns voce acertou o numero, o numero era {numeroSecreto}")

