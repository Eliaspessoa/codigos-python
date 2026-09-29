#crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. depois mostre
#(A) Apenas os 5 primeiros colocados.
#(B) Os últimos 4 colocados da tabela.
#(C) Uma lista com os times em ordem alfabética.
#(D) em que posição na tabela estpa o time da chapecoense.

times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Bragantino', 'Atletico-Paranaense', 'Bahia', 'Coritiba', 'São Paulo', 'Botafogo', 'EC Vitória' , 'Atlético-Mineiro', 'Corinthans', 'Cruzeiro', 'Internacional', 'Santos','Grêmio','Vasco da Gama', 'Mirassol', 'Remo', 'Chapecoense')

print(f'Lista de  times do Brasileirão: {times}')
print("="*15)
print("Os Cincos Primeiros colocados são:")
for clube in times[:5]:
    print(clube)
print("="*15)
print("Os cincos ultimos colocados são: ")
for clube in times[15:21]:
    print(clube)
print("="*15)
print("A classificação por ordem Alfabetica são :")
for clube in sorted(times):
    print(clube)
print("="*15)
print(f'A posição da chapecoense no Brasileirão é na {times.index('Chapecoense')+1} Posição')
print("="*15)
