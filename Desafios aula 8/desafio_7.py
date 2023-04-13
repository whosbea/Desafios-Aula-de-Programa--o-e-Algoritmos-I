accountnumber = input("Qual o numero da sua conta?")
balance = float(input("Qual seu saldo?"))
debit = float(input("Qual seu débito?"))
credit = float(input("Qual seu crédito?"))
atualbalance = (balance - debit + credit)

if atualbalance >= int(0):
    print(f"Saldo Positivo. Seu saldo é: {atualbalance}")
else:
    print(f"Saldo negativo. Seu saldo é: {atualbalance}")