meus_itens = []

while True:
    item = input("Digite um item para adicionar a lista (ou 'sair' para encerrar):")
    if item.lower() == 'sair':
        break
    meus_itens.append(item)

    meus_itens.sort()  # Ordena a lista em ordem alfabética

print("Itens adicionados à lista:")
for i, item in enumerate(meus_itens, start=1):
    print(f"{i}. {item}")