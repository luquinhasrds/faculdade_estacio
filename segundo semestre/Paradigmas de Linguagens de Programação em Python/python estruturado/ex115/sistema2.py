from lib.interface.arquivo_pessoas_novo import Cadastro, Pessoa
from lib.interface import *

cadastro = Cadastro()

while True:
    opcao = menu(['Cadastrar pessoa', 'Listar pessoas', 'Sair', 'Limpar arquivo de cadastro'])

    if opcao == 1:
        cabecalho('CADASTRO')
        nome = input('Digite seu nome:').capitalize()
        idade = leiaInt('Digite sua idade: ')
        pessoa = Pessoa(nome, idade)
        cadastro.adicionar_pessoa(pessoa)
    elif opcao == 2:
        cabecalho('PESSOAS CADASTRADAS')
        cadastro.listar_pessoas()
    elif opcao == 3:
        fechar_programa('Fechando o programa...')
        break
    elif opcao == 4:
        cadastro.limpar_lista()