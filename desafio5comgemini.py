produtos = []
print('-' * 60)
print("Bem-vindo ao sistema de cadastro de produtos!")
print('-' * 60)
while True:
    try:
        nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
        print('-' * 60)
        
        if nome.lower() == 'sair':
            break
        
        elif nome.strip():  # Verifica se o nome não é vazio
            preco = float(input("Digite o preço do produto: "))
            
            if preco < 0:
                print("Atenção: O preço do produto é negativo.")
            
            else:
                produtos.append({'nome': nome, 'preco': preco})   
                print(f"Produto '{nome}' cadastrado com sucesso!")
        else:
            print("Entrada inválida. Por favor, digite um nome de produto válido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um nome de produto válido.")
print('-' * 60)

print("\nLista de produtos cadastrados:")
for produto in produtos:
    print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

soma_total = sum(produto['preco'] for produto in produtos)
print('-' * 60)
print(f"\nSoma total dos preços dos produtos: R${soma_total:.2f}")
quantidade = len(produtos)

if quantidade > 0:
    media = soma_total / quantidade
    print(f"Média dos preços dos produtos: R${media:.2f}")
else:
    print("Nenhum produto cadastrado para calcular a média.")

#print('-' * 60)
#print(f"Média dos preços dos produtos: R${media:.2f}")
#print('-' * 60)

print("\nObrigado por utilizar o sistema de cadastro de produtos!")
print('-' * 60)