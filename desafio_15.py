Ganho_Hora = float(input())
Hora_Trabalhada = float(input())
Salario = (Ganho_Hora * Hora_Trabalhada)
IR = Salario * 0.11
INSS = Salario * 0.08
SIND = Salario * 0.05
Salario_Liquido = Salario - (IR + INSS + SIND)

print(f"Salário Bruto: R${Salario:.2f}")
print(f"IR (11%): R${IR}")
print(f"INSS (8%): R${INSS}")
print(f"SIND (5%): R${SIND}")
print(f"Salário Liquido: R${Salario_Liquido:.2f}")