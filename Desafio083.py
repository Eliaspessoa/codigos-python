#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a Expressão: '))
pilha = list()
for s in expressao:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta o formato!')
else:
    print('Sua expressão não está correta , tente novamente!')