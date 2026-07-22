  #Faça um programa que leia um  número inteiro e diga se ele é ou não um número primo.
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1 ):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\033[mO Número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é Primo')
else:
    print('E por isso ele não é Primo')