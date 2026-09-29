#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O numero {} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O numero {} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O numero {} convertudo para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida')