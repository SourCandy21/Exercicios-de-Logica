# fazer um exercício que peça um nota, entre zero a dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe uma valor valido
 

while True:
  print("Digite uma nota entre 0 e 10: ")
  try:
    nota = int(input())
    if 0 <= nota <= 10:
      break
    else:
      print("Valor inválido. ")
  except ValueError:
    print("Valor inválido. ")

print("Você digitou a nota:", nota)
 
 