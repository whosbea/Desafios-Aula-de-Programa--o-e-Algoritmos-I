nDia = int(input("Digite um numero de 1 a 7 que direi o dia da semana correspondente a esse numero!\n"))

if nDia == 1:
    print(f"O numero {nDia} corresponde ao Domingo.")

elif nDia == 2:
    print(f"O numero {nDia} corresponde a Segunda.")

elif nDia == 3:
    print(f"O numero {nDia} corresponde a Terça.")

elif nDia == 4:
    print(f"O numero {nDia} corresponde a Quarta.")

elif nDia == 5:
    print(f"O numero {nDia} corresponde a Quinta.")

elif nDia == 6:
    print(f"O numero {nDia} corresponde a Sexta.")

elif nDia == 7:
    print(f"O numero {nDia} corresponde ao Sábado.")

else:
    print("Opa, não existe nenhum dia da semana com esse numero, escolha outro por favor.")