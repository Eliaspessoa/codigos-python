#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
#(A) Quantas vezes apareceu o valor 9.
#(B) Em que posição foi digitado o primeiro valor 3.
#(C) quais foram os números pares.
num = (int(input('Digite um número: ')),
        int(input('Digite segundo número: ')),
        int(input('Digite terceiro número: ')),
        int(input('Digite quarto número: ')))

print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('o valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')









