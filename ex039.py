#Façã um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se aliastar.
# - Se já passou do tempo do alistamento.
#Seu Programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date


def verificar_prazo_alistamento(ano_nascimento):
    # 1. Obter o ano atual
    ano_atual = date.today().year

    # 2. Calcular a idade usando o ano de nascimento fornecido
    # É fundamental que a variável 'ano_nascimento' (parâmetro) não seja sobrescrita antes de calcular a idade.
    idade = ano_atual - ano_nascimento

    # Idade para o alistamento militar obrigatório no Brasil
    IDADE_ALISTAMENTO = 18

    print(f'Quem nasceu em {ano_nascimento} tem ->->{idade}<-<- anos em {ano_atual}.')
    print("-" * 30)

    # 3. Verificar a situação do alistamento

    if idade < IDADE_ALISTAMENTO:
        # Ainda vai se alistar
        saldo = IDADE_ALISTAMENTO - idade
        ano_alistamento = ano_atual + saldo
        print('Situação: **Ainda vai se alistar**.')
        print(f'Ainda faltam **{saldo}->-> ano(s) para o alistamento.')
        print(f'Seu alistamento será em ->->{ano_alistamento}<-<-.')

    elif idade == IDADE_ALISTAMENTO:
        # Hora de se alistar
        print('Situação: ->-> É a hora de se alistar<-<-!')
        print('Procure a Junta de Serviço Militar mais próxima imediatamente.')

    else:  # idade > IDADE_ALISTAMENTO
        # Já passou do tempo
        saldo = idade - IDADE_ALISTAMENTO
        ano_alistamento = ano_atual - saldo
        print('Situação: ->-> Já passou do tempo do alistamento<-<-.')
        print(f'Você já deveria ter se alistado há ->->{saldo}<-<- ano(s).')
        print(f'O seu ano de alistamento foi em ->->{ano_alistamento}<-<-.')


# --- Ponto de Entrada do Programa ---
try:
    # Capturar e validar a entrada do usuário
    nascimento = int(input('Digite o ano de nascimento (ex: 2006): '))

    # Validação simples para evitar anos futuros ou muito antigos
    if nascimento > date.today().year or nascimento < date.today().year - 120:
        print("Ano de nascimento inválido.")
    else:
        verificar_prazo_alistamento(nascimento)

except ValueError:
    print('Entrada Inválida. Por favor, digite um número inteiro.')

