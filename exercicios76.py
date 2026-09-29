#crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,na sequencia. No final,mostre uma listagem de preços, organizando os dados em forma tabular.
cabecalho = ("PRODUTO", "PREÇO")

tabela = [
    ("Banana", 3.50),
    ("Laranja", 6.70),
    ("Uva", 9.20),
    ("Pera", 10.20),
]
print('=-' * 35)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=-' * 35)
print(f'{cabecalho[0]:<20} | {cabecalho[1]:>10}')
print('=-' * 35)

for nome, preco in tabela:
    # O formatador :.2f garante duas casas decimais para o preço
    print(f"{nome:<20} | R$ {preco:>8.2f}")

print('=-' * 35)