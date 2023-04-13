number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 == number2 == number3 or number1 == number2 or number1 == number3 or number2 == number3:
    print('Os númeos não podem ser iguais.')
else:
    lista = [number1, number2, number3]
    print(sorted(lista))
