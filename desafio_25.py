apple = int(input('Digite a quantidade de maçãs que você quer: '))
strawberry = int(input('Digite a quantidade de morango que você quer: '))

apple_counter = 0
strawberry_counter = 0
price = float (0) 

while(apple_counter < apple):
    apple_counter = apple_counter + 1      
    if apple_counter < 5:
        price = price + 1.8
    else:
         price = price + 1.5

while(strawberry_counter < strawberry):
    strawberry_counter = strawberry_counter + 1
    if strawberry_counter < 5:
            price = price + 2.5    
    else:
         price = price + 2.2

if apple + strawberry >= 8 or price > 25:
    price = price * 0.9
    
print('O preço do morango e da maçã é: R$ ' , end="")
print(price)