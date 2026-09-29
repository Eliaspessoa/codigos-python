#Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Digite um numero: "))
print("-----------")
for n in range(1, 11):
    print("{} x {} = {}".format(numero, n, numero*n))
print("-----------")