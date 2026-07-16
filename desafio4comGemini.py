class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def ordenar(self):
        self.itens.sort()
    
    def exibir(self):
        print('Itens adicionados à lista:')
        for i, item in enumerate(self.itens, start=1):
            print(f"{i}. {item}")

minha_lista = ListaDeCompras()
while True:
    item = input("Digite um item para adicionar à lista (ou 'sair' para encerrar): ")
    if item.lower() == 'sair':
        break
    minha_lista.adicionar(item)
    minha_lista.ordenar()
minha_lista.exibir()    