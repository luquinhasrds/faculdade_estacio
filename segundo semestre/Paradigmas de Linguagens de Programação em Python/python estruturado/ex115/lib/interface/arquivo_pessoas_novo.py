from lib.interface import *

# Cores ANSI para terminal
VERDE_BRILHANTE = '\033[92m'
VERDE = '\033[32m'
VERMELHO_BRILHANTE = '\033[91m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f"{self.nome, {self.idade}}"
    
class Cadastro:
    def __init__(self, arquivo = 'cadastro de pessoas.txt'):
        self.arquivo = arquivo
        
    def adicionar_pessoa(self, pessoa):
        try:
            with open(self.arquivo, 'a') as f:
                f.write(f'{pessoa.nome};{pessoa.idade}\n')
        except Exception as e:
            print(f'{VERMELHO}Erro ao escrever no arquivo: {e}{RESET}')
        else:
            print(f'{VERDE_BRILHANTE}Pessoa {pessoa.nome} cadastrada com sucesso no arquivo!{RESET}')
            
    def listar_pessoas(self):
        try:
            with open(self.arquivo, 'r') as f:
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
            
    def limpar_lista(self):
        while True:
            opcao = input('Tem certeza que deseja limpar o arquivo (S/N) ?').upper()
            if opcao == 'S':
                try:
                    with open(self.arquivo, 'r') as f:
                        conteudo = f.read()
                        if not conteudo.strip():
                            print(F'{VERDE}Arquivo ja está vazio.{RESET}')
                            print('Voltando ao menu.')
                            break
                        else:
                            with open(self.arquivo, 'w') as f:
                                f.write('')
                                print(f'{VERDE}Lista limpa.{RESET}')
                                break
                except FileNotFoundError:
                    print(f'{VERMELHO}ARQUIVO NÃO ENCONTRADO.{RESET}')
                except Exception as erro:
                    print(f'{VERMELHO}ALGO DEU ERRADO: {erro}{RESET}')
            elif opcao == 'N':
                print('Voltando ao menu.')
                break
            else:
                print(f'{VERMELHO_BRILHANTE}Responda corretamente por favor!!{RESET}')
                continue