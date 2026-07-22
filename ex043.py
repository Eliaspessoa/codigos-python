#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC e mostre seu status,de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do Peso
# -Entre 18.5 e 25: Peso ideal
# -25 até 30:Sobrepeso
# -30 até 40:Obesidade
# -Acima de 40: Obesidade mórbida

peso = int(input('Digite o seu Peso: '))
altura = float(input('Digite sua Altura: '))
imc = peso / (altura ** 2)
print('O Imc dessa pessoa é de {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você esta Abaixo do peso')
elif imc == 18.5 and imc < 25:
    print('Você esta com Peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você esta com Obesidade')
else:
    print('Você está com Obesidade mórbida')