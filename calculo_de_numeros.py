# Um programa que peça dois numero inteiros e imprima a soma desses números  

num1 = 0 
num2 = 0

while  num1 == 0:
    num1 = int(input("Digite um numero inteiro: "))
    if num1 == 0:
        print("Digite um numero inteiro valido")
        num1 = 0

while num2 == 0:
    num2 = int(input("Digite outro numero inteiro: "))
    if num2 == 0:
        print("Digite um numero inteiro valido")
        num2 = 0

print("A soma dos numeros é: ", num1 + num2)
