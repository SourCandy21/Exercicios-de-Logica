#Um progrma que leia um valor em metros e o exiba convertido em milimetros

metros = 0
while metros == 0:
    metros = float(input("Digite um valor em metros: "))
    if metros == 0:
        print("Digite um valor valido")

        metros = 0

print("O valor em milimetros é: ", metros * 1000)
