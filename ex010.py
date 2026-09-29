real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.33
euro = real / 6.23
print('Com R${:.2f} você pode comprar US$ {:.2f} dolar'.format(real, dolar))
print('Com R${:.2f} você pode comprar EURO$ {:.2f} euro'.format(real, euro))

