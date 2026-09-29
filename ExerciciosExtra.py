while True:
    print("-" * 69)
    try:
        altura = float(input("Digite sua altura em metros:(Digite ex: 1.70 ou digite 0 para parar):  "))
        if altura == 0:
            print("Encerrando o sistema ......")
            print("-" * 69)
            break
        peso   = float(input("Digite sua massa em kilogramas: "))
        imc = peso / (altura * altura)

        
        if imc < 18.5:
            print('Voce esta Abaixo do peso')
        elif imc >= 18.5 and imc < 25:
            print('Voce esta com Peso Normal')
        elif imc >= 25 and imc < 30:
            print('Voce esta com Sobrepeso')
        elif imc >= 30 and imc < 40:
            print('Voce esta com Obesidade')
        else:
            print('Voce esta em obesidade grave')

    except ValueError:
        print("Erro ao calcular")

