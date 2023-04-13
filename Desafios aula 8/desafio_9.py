nempregado = input("Informe o numero do empregado:")
anonascimento = int(input("Informe o ano de nascimento:"))
anoingresso = int(input("Informe o ano de ingresso:"))
anoatual = int(input("Ano atual:"))
Idade = (anoatual - anonascimento)
tempotrab = (anoatual - anoingresso)

if Idade >= int(65):
    print(f"Idade: {Idade}\nTempo trabalhado: {tempotrab}\nRequerer aposentadoria")
elif Idade >= int(60) and tempotrab >= int(25):
    print(f"Idade: {Idade}\nTempo trabalhado: {tempotrab}\nRequerer aposentadoria")    
elif tempotrab >= int(30):
    print(f"Idade: {Idade}\nTempo trabalhado: {tempotrab}\nRequerer aposentadoria")

else:
    print(f"Idade: {Idade}\nTempo trabalhado: {tempotrab}\nNão requerer aposentadoria")