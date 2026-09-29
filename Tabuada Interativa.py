import time

while True:
    num = int(input("Qual tabuada você quer ver? (ou 99 para sair): "))

    if num == 99:
        for y in range(5):

            print(f"Finalizando em {5 - y}...", end="\r", flush=True)
            time.sleep(1)

            print()  # <--- ISSO AQUI pula para a linha de baixo

        break

    elif num < 10:
        # AQUI você coloca o loop 'for' que vai criar o 'i'
        for i in range(1, 11):
            resultado = num * i
            print(f'{num} x {i} = {resultado}')
    elif num > 10:
        print('O número é inválido (maior que 10)')