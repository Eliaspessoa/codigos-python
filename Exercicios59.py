#Crie um programa que leia dois valores e mostre um menu na tela:1:somar,2:multiplicar,3:maior,4:novos números,5:sair do programa, Seu programa deverá realizar a operação solicitada em cada casa
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0

while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa
    ''')
    opção = int(input('>>>>> Qual é a sua opção? '))

    if opção  == 1:
        opção = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, opção))
    elif opção == 2:
        opção = n1 * n2
        print('A Multiplicação entre {} x {} é {}.'.format(n1, n2, opção))
    elif opção == 3:
        if n1 > n2:
            print('Primeiro valor é Maior: {}'.format(n1))
        if n1 < n2:
            print('Primeiro valor é Menor: {}'.format(n2))
        if n1 == n2:
            print('Os valor {} e o valor {} são iguais.'.format(n1, n2))
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção != 5:
        print('Opção Invalida')
    else:
        print('Fim')


