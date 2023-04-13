import random

lista = ['pedra','papel','tesoura']
escolha_jogador = input("Escolha pedra, papel ou tesoura:\n")
escolha_pc = random.choice(lista)

while escolha_jogador == escolha_pc:
    print("Empatou, tente novamente.")
    escolha_jogador = input("Escolha pedra, papel ou tesoura:\n")
    escolha_pc = random.choice(lista)

if escolha_jogador == "pedra" and escolha_pc == "tesoura":
    print(f"O computador escolheu {escolha_pc} e voce escolheu {escolha_jogador}\n")
    print("O voce ganhou!")
elif escolha_pc == "pedra" and escolha_jogador == "tesoura":
    print(f"O computador escolheu {escolha_pc} e voce escolheu {escolha_jogador}\n")
    print("O computador venceu!")
elif escolha_jogador == "papel" and escolha_pc == "pedra":
    print(f"O computador escolheu {escolha_pc} e voce escolheu {escolha_jogador}\n")
    print("O voce ganhou!")
elif escolha_jogador == "pedra" and escolha_pc == "papel":
    print(f"O computador escolheu {escolha_pc} e voce escolheu {escolha_jogador}\n")
    print("O computador venceu!")
elif escolha_jogador == "tesoura" and escolha_pc == "papel":
    print(f"O computador escolheu {escolha_pc} e voce escolheu {escolha_jogador}\n")
    print("O voce ganhou!")
elif escolha_jogador == "papel" and escolha_pc == "tesoura":
    print(f"O computador escolheu {escolha_pc} e voce escolheu {escolha_jogador}\n")
    print("O computador venceu!")
#while escolha_jogador != "pedra""papel""tesoura":
   # print("essa opção não exite tente dnv")
   # escolha_jogador = input("Escolha pedra, papel ou tesoura:\n")
   # escolha_pc = random.choice(lista)
