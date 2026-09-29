# Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.No final,Mostre:
# A) Quantas Pessoas tem mais de 18 anos. B)Quantas homens foram cadastrados. C)Quantas mulheres tem menos de 20 anos.

tot18 = tot_homens = tot_mulheres_20 = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    
    idade = int(input("Idade: "))
    
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        
    if idade > 18:
        tot18 += 1
        
    if sexo == "M":
        tot_homens += 1
        
    if sexo == "F" and idade < 20:
        tot_mulheres_20 += 1
        
    print("-" * 30)
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        
    if resp == "N":
        break

print("=" * 30)
print("FIM DO PROGRAMA")
print("=" * 30)
print(f"A) Total de pessoas com mais de 18 anos: {tot18}")
print(f"B) Total de homens cadastrados: {tot_homens}")
print(f"C) Total de mulheres com menos de 20 anos: {tot_mulheres_20}")