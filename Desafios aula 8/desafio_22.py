valor = int(input("Digite o valor em Reais: "))

notas_100 = valor // 100
valor %= 100

notas_50 = valor // 50
valor %= 50

notas_10 = valor // 10
valor %= 10

notas_5 = valor // 5
valor %= 5

notas_1 = valor

print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 1: {notas_1}")