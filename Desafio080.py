#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for numero in range (0, 5):
    nu = int(input('Digite um valor: '))
    if numero == 0 or nu > lista[-1]:
        lista.append(nu)
        print('Adicionado ao final com sucesso ')
    else:
        pos = 0
        while pos < len(lista):
            if nu <= lista[pos]:
                lista.insert(pos, nu)
                print(f'Foi adicionado na posição {pos} da lista ..')
                break
            pos += 1
print('=' * 30)
print(f'Os valores digitados em ordem foram {lista}')