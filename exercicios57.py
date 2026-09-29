#Faça um programa que leia o sexo de uma pessoa,mas só aceite os valores 'M' ou 'F'.Caso esteja errado,peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()
    if sexo == 'M'or sexo == 'F':
        print('Sexo cadastrado com sucesso!')
    else:
        print('Opção Invalida')

print('Fim')
