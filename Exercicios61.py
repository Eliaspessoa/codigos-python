#Refaça o Desafio 051,lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
decimo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro = primeiro + razão
    cont += 1
print('Fim')
