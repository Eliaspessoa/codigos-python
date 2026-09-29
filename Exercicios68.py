#Faça um programa que jogue par ou ímpar com o computador.O jogo só será interrompido quando o jogador PERDER, Mostrando o total de vitórias conscutivas que ele conquistou no final do jogo.
from random import randint

vitorias = 0

print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    
    while tipo not in "PI":
        tipo = str(input("Par [P] ou Ímpar [I]? ")).strip().upper()[0]
        
    print("-" * 30)
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total} ", end="")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    print("-" * 30)
    
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if total % 2 != 0:
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break
            
    print("Vamos jogar novamente...\n")

print("=-" * 15)
print(f"GAME OVER! Você venceu {vitorias} vezes consecutivas.")