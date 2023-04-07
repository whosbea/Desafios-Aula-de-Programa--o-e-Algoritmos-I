time1 = input("Qual nome do primeiro time ? ")
gols1 = int(input("Quantos gols ele fez ? "))
time2 = input("Qual nome do segundo time ? ")
gols2 = int(input("Quantos gols ele fez ? "))

if gols1 > gols2:
    print(f"O time {time1} amassou o {time2}de {gols1}x{gols2}")
if gols1 < gols2:
    print(f"O time {time2} amassou o {time1} de {gols2}x{gols1}")
else:
    print(f"Empatou, o placar foi {gols1}x{gols2}")