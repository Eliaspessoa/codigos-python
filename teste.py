
while True:
    
    sexo = str(input('Digite o sexo para cadastrar [m/f]:  ')).upper()
    if sexo in 'MF': 
        print('Sexo cadastrado')
        break
        
    else:
        print('Digite o sexo correto!')
        