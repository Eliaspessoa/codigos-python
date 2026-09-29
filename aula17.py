valores = []
valores.append(10)
valores.append(11)
valores.append(12)

del valores[2]

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')