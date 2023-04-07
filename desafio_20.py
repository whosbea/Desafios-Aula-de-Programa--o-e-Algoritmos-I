menu = {
    '100': 1.20,
    '101': 1.30,
    '102': 1.50,
    '103': 1.20,
    '104': 1.70,
    '105': 2.20,
    '106': 1.00,
}

codigo = input("Digite  o código do produto: ")
quantidade = int(input("Digite a quantidade desejada: "))

if codigo not in menu:
    print ("Código do produto inválido:")
else:
    preco = menu[codigo] * quantidade
    print(f"Preço total: R${preco:.2f}")