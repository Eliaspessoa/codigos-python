#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis','sete','oito', 'nove',
        'dez', 'onze', 'doze', 'treze','catorze',
        'quinze','dezesseis','dezessete','dezoito',
        'dezenoveze','vinte')
while True:
    num1 = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num1 <= 20:
        break

print(f'você digitou o número {cont[num1]}')


