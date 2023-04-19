estoque = "| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |"

print(estoque)
acao = input("O que deseja fazer? [1] - Adicionar um produto [2] - Pesquisar produto [3] - Vender produto\n")

if acao == "1":
    produto = input("Qual produto você quer adicionar? [1] - Camisa [2] - Calça [3] - Vestido \n")
    tamanho = input("Qual tamanho do produto P , M ou G? \n")
    qnt_add = int(input("Qual a quantidade você quer adicionar? \n"))
    if produto == "1":
        qnt_produto = 1 + qnt_add
        match tamanho:   
            case "P":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| {qnt_produto} - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
            case "M":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| {qnt_produto} - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
            case "G":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| {qnt_produto} - G  | 1 - G |  1 - G  |")
    elif produto == "2":
        qnt_produto = 1 + qnt_add
        match tamanho:   
            case "P":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | {qnt_produto} - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
            case "M":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | {qnt_produto} - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
            case "G":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | {qnt_produto} - G |  1 - G  |")
    elif produto == "3":
        qnt_produto = 1 + qnt_add
        match tamanho:   
            case "P":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  {qnt_produto} - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
            case "M":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  {qnt_produto} - M  |\n| 1 - G  | 1 - G |  1 - G  |")
            case "G":
                print(f"\nO produto foi adicionado ao estoque.\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  {qnt_produto} - G  |")
elif acao == "2":
    pesquisa = input("Que produto você quer pesquisar?\n")
    match pesquisa:
        case "camisa":
            print("Esse produto está no seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
        case "calça":
            print("Esse produto está no seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
        case "vestido":
           print("Esse produto está no seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
        #case !=:
            #print("Infelizmente esse produto não está no seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
elif acao == "3":
    venda = input("Qual produto você vendeu? [1] - Camisa [2] - Calça [3] - Vestido\n")
    match venda:
        case "1":
            tamanho = input("Qual tamanho de camisa foi vendido? P, M ou G \n")
            match tamanho: 
                case "P":
                    print(f"O tamanho {tamanho} de camiseta foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n|   -    | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
                case "M":
                    print(f"O tamanho {tamanho} de camiseta foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n|   -    | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
                case "G":
                    print(f"O tamanho {tamanho} de camiseta foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n|   -    | 1 - G |  1 - G  |")
        case "2":
            tamanho = input("Qual tamanho de calça foi vendido? P, M ou G \n")
            match tamanho:
                case "P":
                    print(f"O tamanho {tamanho} de calça foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  |   -   |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
                case "M":
                    print(f"O tamanho {tamanho} de calça foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  |   -   |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
                case "G":
                    print(f"O tamanho {tamanho} de calça foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  |   -   |  1 - G  |")
        case "3":
            tamanho = input("Qual tamanho de vestido foi vendido? P, M ou G \n")
            match tamanho:
                case "P":
                    print(f"O tamanho {tamanho} de vestido foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |    -    |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |  1 - G  |")
                case "M":
                    print(f"O tamanho {tamanho} de vestido foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |    -    |\n| 1 - G  | 1 - G |  1 - G  |")
                case "G":
                    print(f"O tamanho {tamanho} de vestido foi vendido e retirado do seu estoque\n| Camisa | Calça | Vestido |\n|--------|-------|---------|\n| 1 - P  | 1 - P |  1 - P  |\n| 1 - M  | 1 - M |  1 - M  |\n| 1 - G  | 1 - G |    -    |")
