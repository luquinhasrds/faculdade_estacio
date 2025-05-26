from classes import Conta
class Extrato:
    def __init__(self, conta):
        self.transacoes = []
        self.conta = conta

    def gerar_extrato(self, conta):
        print(f'Extrato da conta: {conta}')
        for tran in self.transacoes:
            print(f'{tran[0]:15s} {tran[1]:10.2f} {tran[2].strftime('%d/%b/%Y')}')
        print(f'Saldo atual: {self.conta.saldo}')



#[0 - Tipo | 1 - valor | 2 - data]