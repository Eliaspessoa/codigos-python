# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador : R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser Concedido!')
else:
    print('Emprestimo Reprovado!')
