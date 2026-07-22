#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

valores = (randint(1, 10 ), randint(1, 10 ), randint(1, 10 ), randint(1, 10 ), randint(1, 10 ))
print("=-" * 35)
print(f"Os valores sorteados foram {valores}")
print("=-" * 35)
print(f"O maior valor sorteado foi {max(valores)}")
print("=-" * 35)
print(f"O menor valor sorteado foi {min(valores)}")
print("=-" * 35)
