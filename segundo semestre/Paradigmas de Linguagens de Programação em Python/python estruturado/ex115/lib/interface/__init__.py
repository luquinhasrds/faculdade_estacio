# Cores ANSI para terminal
VERDE_BRILHANTE = '\033[92m'
VERDE = '\033[32m'
VERMELHO_BRILHANTE = '\033[91m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

from tabulate import tabulate

def leiaInt(txt):
    while True:
        try: 
            n = int(input(txt))
        except:
            print(f'{VERMELHO_BRILHANTE}Digite um numero inteiro valido!!!{RESET}')
            continue
        else:
            return n 
        

def linha(tam = 42):
    return print('-' * tam)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    cabecalho('SISTEMA')
    c = 1
    for items in lista:
        print(f'{c} - {items}')
        c += 1
    opc = leiaInt('Digite uma opção: ')
    return opc

def fechar_programa(txt):
    linha()
    print(f'{VERDE_BRILHANTE}{txt}{RESET}')
    linha()