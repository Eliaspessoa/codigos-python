#melhore o jogo do Desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.Só que agora o jogador vai tentar adivinhar até acertar,mostrando no final quantos palpites foram necessessãrios para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
tentativas = 0
palpites = -1
print('Jogo Da Adivinhação! Tente acertar o um número entre 0 e 10')
sleep(2.0)

while palpites != computador:
    palpites = int(input('Qual é o seu Palpite Marreco?(0 a 10) '))
    tentativas += 1
    if palpites < computador:
        print('Mais.... Tente novamente!')
        sleep(1)
    elif palpites > computador:
        print('Menos.... Tente novamente!')

print('Parabéns !Voce acertou cara ! o número era {}.'.format(computador))
print('E foram no total de {} tentativas.'.format(tentativas))
