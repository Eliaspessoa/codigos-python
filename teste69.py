h1 = 0
h2 = 0
tot18 = 0

while True:
    idade=int(input('digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo=str(input('digite seu sexo (M/F)')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
           h1 += 1
    if sexo == 'F' and idade < 20:
            h2 += 1
    resp = ' '
    while resp not in 'SN':
        resp=str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('a quantidade exata de homens são de {}'.format(h1))
print('e a quantidade de mulheres são {}'.format(h2))
print('e a quantidades de mulheres menores de 20 anos são de {}'.format(tot18))


