salario_anual = float(input("Digite o salario anual familiar: "))
qnt_dependentes = int(input("Informe a quantidade de dependentes"))

salario_mensal = salario_anual / 12
total_de_pessoas = qnt_dependentes + 1
media_per_capta = salario_mensal / total_de_pessoas

if media_per_capta <= 1903.98:
    print("Você está insento.")
elif media_per_capta <= 2826.65:
    imposto = (media_per_capta * 0.075) + 142.80
    print("Voce deve pagar R${:.2f}".format(imposto))
elif media_per_capta <= 3751.05:
    imposto = (media_per_capta * 0.15) + 354.80
    print("Voce deve pagar R${:.2f}".format(imposto))
