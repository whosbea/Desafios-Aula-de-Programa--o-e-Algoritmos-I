lado1 = float(input("Insira o lado 1: "))
lado2 = float(input("Insira o lado 2: "))
lado3 = float(input("Insira o lado 3: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    if lado1 != lado2 != lado3:
        print("O triangulo é escaleno.")
    elif lado1 != lado2 or lado1 != lado3 or lado2 != lado3:
        print("O triangulo é isósceles.")
    elif lado1 == lado2 == lado3:
        print("O triangulo é equilátero.")
else:
    print("Não é possivel fazer um triângulo.")