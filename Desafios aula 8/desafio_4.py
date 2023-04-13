salario = float(input("Qual seu salario? "))
emprestimo = float(input("Qual valor do emprestimo desejado? "))
qntMeses = int(input("Qual a quantidade de meses? "))

prestacao = emprestimo / qntMeses
limite = 0.2 * salario

if prestacao > limite:
    print("Ih não da não mano, teu a prestação é 20% maior que teu salario")

else:
    print(f"Valor da prestação é: R$ {prestacao}/mes")