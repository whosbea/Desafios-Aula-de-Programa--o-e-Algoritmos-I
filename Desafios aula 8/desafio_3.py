n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
operacao = str(input("Qual operação você quer fazer? "))

if operacao == "+":
    soma = n1 + n2
    print(f"O resultado foi: {soma}")

if operacao == "-":
    subtracao = n1 - n2
    print(f"O resultado é: {subtracao}")

if operacao == "*":
    multiplicacao = n1 * n2
    print(f"O resultado é: {multiplicacao}")

if operacao == "/":
    divisao = n1/n2 
    print(f"O resultado é: {divisao}")