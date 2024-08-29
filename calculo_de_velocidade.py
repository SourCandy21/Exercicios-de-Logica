#Um programa que calcule o tempo de uma viagem de carro. Pergunte a distância e a velocidade média esperada para a viagem 

velocidade = 0
distancia = 0

while velocidade == 0:
    velocidade = float(input("Digite a velocidade media: "))
    if velocidade == 0:
        print("Digite um valor valido")
        velocidade = 0

while distancia == 0:
    distancia = float(input("Digite a distancia: "))
    if distancia == 0:
        print("Digite um valor valido")
        distancia = 0

print("O tempo da viagem é: ", distancia / velocidade)

