#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.No final,Mostre:
#A)Qual é o total gasto na compra. B)Quantos produtos custam mais de R$1000.  C)Qual é o nome do produto mais barato.

total_gasto = produtos_mais_mil = menor_preco = 0
barato = ""
primeiro = True

while True:
    print("-" * 30)
    print("LOJA SUPER BARATO")
    print("-" * 30)
    
    nome = str(input("Nome do Produto: ")).strip()
    preco = float(input("Preço: R$ "))
    
    total_gasto += preco
    
    if preco > 1000:
        produtos_mais_mil += 1
        
    if primeiro or preco < menor_preco:
        menor_preco = preco
        barato = nome
        primeiro = False
        
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        
    if resp == "N":
        break

print("=" * 30)
print("FIM DO PROGRAMA")
print("=" * 30)
print(f"A) O total gasto na compra foi R$ {total_gasto:.2f}")
print(f"B) Temos {produtos_mais_mil} produtos custando mais de R$ 1000.00")
print(f"C) O produto mais barato foi {barato} que custa R$ {menor_preco:.2f}")