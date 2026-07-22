import random
computador = random.randint(1, 10)
tentativa = 0
while True:
    try:
        jogador = int(input("Digite um número de 1 a 10: "))
        tentativa += 1
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    
    if jogador == computador:
        print("Parabéns! voce acertou!")
        print(f"Você acertou em {tentativa} tentativas.")
        break
    elif jogador < computador:
        print("O número que voce chutou é menor tente novamente.")
    else:
        print("O número que voce chutou é maior tente novamente.")
    
    

print(f"O número que o computador escolheu foi: {computador}")