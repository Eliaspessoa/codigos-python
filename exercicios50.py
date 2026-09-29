#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.Se o valor digitado for impar,desconsidere-o.
soma = 0
cont = 0
for nu in range(1, 7):
    valor = int(input(f"Digite um numero: "))
    if valor % 2 == 0:
        soma += valor
        cont += 1
print('Você informou {} números Pares e a soma entre eles ficaram em {}.'.format(cont, soma))



