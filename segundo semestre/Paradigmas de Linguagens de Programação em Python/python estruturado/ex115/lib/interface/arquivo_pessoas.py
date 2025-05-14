from lib.interface import *

# Cores ANSI para terminal
VERDE_BRILHANTE = '\033[92m'
VERDE = '\033[32m'
VERMELHO_BRILHANTE = '\033[91m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

def cadastrar_pessoa(nome, idade, arquivo='cadastro de pessoas.txt'):
    try:
        with open(arquivo, 'a') as f:
            f.write(f'{nome};{idade}\n')
    except Exception as e:
        print(f'{VERMELHO}Erro ao escrever no arquivo: {e}{RESET}')
    else:
        print(f'{VERDE_BRILHANTE}Pessoa {nome} cadastrada com sucesso no arquivo!{RESET}')
        
def listar_pessoas(arquivo='cadastro de pessoas.txt'):
    try:
        with open(arquivo, 'r') as f:
            pessoas = [linha.strip().split(';') for linha in f]
            if pessoas:
                cabecalho('Pessoas cadastradas')
                print(tabulate(pessoas,headers=['Nome', 'Idade'], tablefmt='grid'))
            else:
                print(f'{VERMELHO}Nenhuma pessoa cadastrada{RESET}')
    except FileNotFoundError:
        print(f'{VERMELHO}Arquivo não encontrado. Nenhuma pessoa cadastrada ainda.{RESET}')
    except Exception as erro:
        print(f'{VERMELHO}Erro ao listar pessoas: {erro}{RESET}')
def limpar_lista(arquivo='cadastro de pessoas.txt'):
    try:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            if not conteudo.strip():
                print(F'{VERDE}Arquivo ja está vazio.{RESET}')
            else:
                with open(arquivo, 'w') as f:
                    f.write('')
                    print(f'{VERDE}Lista limpa.{RESET}')
    except FileNotFoundError:
        print(f'{VERMELHO}ARQUIVO NÃO ENCONTRADO.{RESET}')
    except Exception as erro:
        print(f'{VERMELHO}ALGO DEU ERRADO: {erro}{RESET}')