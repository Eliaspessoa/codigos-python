#A confederação Nacional de Natação prescisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 Anos:Mirin
# -Até 14 Anos:Infantil
# -Até 19 Anos: Junior
# -Até 20 Anos: Sênior
# -Acima : Master
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O Atleta tem {} anos'.format(idade))
if idade <= 9:
    print('O Atleta é Mirin')
elif idade <= 14:
    print('O Atleta é Infantil')
elif idade <= 19:
    print('O Atleta é Junior')
elif idade <= 25:
    print('O Atleta é Sênior')
else:
    print('O Atleta é Master')