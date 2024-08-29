#Um programa que calcule o aumentar de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = 0
aumento = 0

while salario == 0:
    salario = float(input("Digite o valor do salario: "))
    if salario == 0:
        print("Digite um valor valido")

        salario = 0

while aumento == 0:
    aumento = float(input("Digite a porcentagem do aumento: "))
    if aumento == 0:
        print("Digite um valor valido")

        aumento = 0

print("O valor do aumento é: ", salario * aumento / 100)
print("O novo salario é: ", salario + salario * aumento / 100)

