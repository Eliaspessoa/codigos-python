#Refaça o Desafio 035 dos triângulos,acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero:todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno : todos os lados diferentes

print('-='* 20)
print('Analisador de Triângulos')
print('-='* 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima Podem Formar UM Triângulo', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('Os segmentos acima nao podem formar um triângulo')
