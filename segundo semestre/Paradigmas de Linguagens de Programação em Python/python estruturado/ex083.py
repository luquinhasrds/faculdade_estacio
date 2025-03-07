expressao = input('DIGITE UMA EXPRESSAO COM PARENTESES: ')
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('deu certo')
else:
    print('deu errado')