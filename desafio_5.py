qntMaca = int(input("Quantas maçãs vc comprou? "))

if qntMaca < 12:
    preco = 2.25 * qntMaca
    print(f"O valor total da sua compra é {preco} reais para {qntMaca} maçãs.")

if qntMaca >= 12: 
    preco = 2 * qntMaca
    print(f"O valor total da sua compra é {preco} reais para {qntMaca} maçãs.")