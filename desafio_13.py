#Álcool: até 20 litros desconto de 3% por litro, acima de 20 litros desconto de 5% por litro

#Gasolina: até 20 litros desconto de 4% por litro, acima de 20 litros desconto de 6% por litro

#litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input("Qual tipo de combustivel você colocou?(Responda com A para Alcool e G para Gasolina) ")
litrosVendidos = float(input(f"Quantos litros de {combustivel} voce botou? "))

g = litrosVendidos * 2.50
a = litrosVendidos * 1.90

if combustivel == "A" and litrosVendidos <= 20:
    valorPago = a * 0.97
    print(f"O total deu R${valorPago:.2f}\nPara {litrosVendidos} litros de Alcool")
elif combustivel == "A" and litrosVendidos > 20:
    valorPago = a * 0.95
    print(f"O total deu R${valorPago:.2f}\nPara {litrosVendidos} litros de Alcool")

elif combustivel == "G" and litrosVendidos <= 20:
    valorPago = g * 0.96
    print(f"O total deu R${valorPago:.2f}\nPara {litrosVendidos} litros de Gasolina")
elif combustivel == "G" and litrosVendidos > 20:
    valorPago = g * 0.94
    print(f"O total deu R${valorPago:.2f}\nPara {litrosVendidos} litros de Gasolina")