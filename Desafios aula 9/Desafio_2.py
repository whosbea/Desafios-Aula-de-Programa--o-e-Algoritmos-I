#Desafio 2
#○ Um programa que receba o valor do produto, o tipo de
#pagamento (1 - Crédito/2 - Débito/3 - Pix/4 - Espécie).
#Caso seja crédito, deve informar a quantidade de
#parcelas.
# O valor final do produto corresponde a:
    #-Pix ou Espécie: 10% de desconto
    #-Débito: 5% de desconto
    #-Crédito:
        #Até 2 vezes: Preço normal
        #Mais que 3 vezes: 20% de acréscimo

valor_produto = float(input("Qual valor do produto? "))
forma_pagamento = input("Qual a forma de pagamento?\n[1]Crédito\n[2]Débito\n[3]Pix\n[4]Espécie\n")

if forma_pagamento == "1":
    parcelas = int(input("Qual numero de parcelas ?"))
    if parcelas <= 2:
        valor_parcela = valor_produto / parcelas
        print(f"O valor final a ser pago é R${valor_produto:.2f} e o valor de cada parcela é R${valor_parcela:.2f}")
    else:
        valor_final = float(valor_produto) * 1.2
        valor_parcela = float(valor_final) / int(parcelas)
        print(f"O valor final é R${valor_final:.2f} e o valor de cada parcela é R${valor_parcela:.2f}")
else:
    if forma_pagamento == "2":
        valor_final = valor_produto * 0.95
        print(f"O valor final a ser pago é R${valor_final:.2f}")
    else:
        if forma_pagamento == "3" or forma_pagamento == "4":
            valor_final = valor_produto * 0.9
            print(f"O valor final a ser pago é R${valor_final:.2f}")