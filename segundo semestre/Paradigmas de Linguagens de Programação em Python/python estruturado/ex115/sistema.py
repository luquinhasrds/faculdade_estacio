from lib.interface import *
from lib.interface.arquivo_pessoas import *

while True:
    opcao = menu(['Cadastrar Pessoa', 'Listar pessoas cadastrada', 'Sair', 'Limpar lista'])

    if opcao == 1:
        cabecalho('CADASTRO')
        nome = input('Digite seu nome:').capitalize()
        idade = leiaInt('Idade:')
        cadastrar_pessoa(nome, idade)
    elif opcao == 2:
        cabecalho('Pessoas cadastradas')
        listar_pessoas()
    elif opcao == 3:
        fechar_programa('Fechando programa...')
        break
    elif opcao == 4:
        limpar_lista()