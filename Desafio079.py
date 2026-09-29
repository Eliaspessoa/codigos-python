#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.No final,serão exibidos todos os valores únicos digitados, em ordem crescente.
import time
valores = []


while True:
    print("-" * 40)
    valor_digitado = int(input('Digite um valor: '))
    if valor_digitado not in valores:
        valores.append(valor_digitado)
        time.sleep(2)
        print("-" * 40)
        print('>>>>Valor Cadastrado com Sucesso<<<<')
    else:
        time.sleep(2)
        print("-" * 40)
        print(">>>>> valor duplicado! não vou adicionar. <<<<")

    time.sleep(1)
    print("-" * 40)

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break


    
print("-" * 40)
# Ordena a lista em ordem crescente
valores.sort()
print(f"Você digitou os valores únicos: {valores}")


    