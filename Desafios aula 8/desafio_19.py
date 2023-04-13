caloria_P = {1: 180, 2: 230, 3: 250, 4: 350}
caloria_S = {1: 75, 2: 110, 3: 170, 4: 200}
caloria_B = {1: 20, 2: 70, 3: 100, 4: 75}


print("| Prato        | Sobremesa           | Bebida               |")
print("| -------------|---------------------|----------------------|")
print("| 1 Vegetariano| 1     Abacaxi       | 1       Chá          |")
print("| 2   Peixe    | 2   Sorvete diet    | 2  Suco de laranja   |")
print("| 3   Frango   | 3    Mouse diet     | 3   Suco de melão    |")
print("| 4   Carne    | 4  Mouse chocolate  | 4  Refrigerante diet |")

prato = int(input("Digite o numero da sua opção de Prato: "))
sobremesa = int(input("Digite o numero da sua opção de Sobremesa: "))
bebida = int(input("Digite o numero da sua opção de Bebida: "))


caloriasTotais = caloria_P[prato] + caloria_S[sobremesa] + caloria_B[bebida]

print(f"O total da calorias do seus pratos é {caloriasTotais} calorias")
