#Um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor de desconto e o preço a pagar 

preco = 0
desconto = 0

while preco == 0:
    preco = float(input("Digite o valor do produto: "))
    if preco == 0:
        print("Digite um valor valido")

        preco = 0

while desconto == 0:
    desconto = float(input("Digite o percentual de desconto: "))
    if desconto == 0:
        print("Digite um valor valido")
        desconto = 0

print("O valor do desconto é: ", preco * desconto / 100)
print("O valor a pagar é: ", preco - preco * desconto / 100)
