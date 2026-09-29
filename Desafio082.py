#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja Continuar: [S/N]:  '))
    if resp in 'Nn':
        break
for v, i in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 == 1:
        impares.append(v)

print(f'Os numeros Digitados foram: {numeros}')
print(f'Os numeros Digitados pares foram: {pares}')
print(f'Os numeros Digitados Impares foram: {impares}')