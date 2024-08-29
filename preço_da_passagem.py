# escrever um programa que pergunte a distância que o passeio deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km, e R$0,45 para viagens mais longas.

print("Digite a distância que deseja percorrer em km: ")
distancia = float(input())
if distancia <= 200:
  preco = distancia * 0.50
else:
  preco = distancia * 0.4
  print("O preço da passagem é: R$", preco)
  