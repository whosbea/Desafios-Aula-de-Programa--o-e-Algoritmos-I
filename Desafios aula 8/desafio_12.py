number1 = int(input("Insira um número inteiro menor que 1000: "))

while number1 >= 1000:
    print("Insira um número menor que 1000: ")
    number1 = int(input())
    
centena = (number1//100)
dezena = (number1%100)//10
unidade = (number1%100)%10
print(f"{centena} centenas, {dezena} dezenas, {unidade} unidades.")