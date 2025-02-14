valor_da_casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salario? '))
tempo = int(input('Em quantos anos voce pretende pagar a casa? '))

valor_da_prestacao = valor_da_casa / (tempo * 12)

if valor_da_prestacao > salario * 0.3:
    print('=-' * 20)
    print('emprestimo negado')
elif valor_da_prestacao <= salario * 0.3:
    print('=-' * 20)
    print('emprestimo aprovado')
    