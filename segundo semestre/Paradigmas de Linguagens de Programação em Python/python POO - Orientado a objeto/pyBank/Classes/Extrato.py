class Extrato:

    def __init__(self):
        self.transacoes = []


    def gerar_extrato(self, conta):
        print(f"Extrato da conta: {conta}")
        for tran in self.transacoes:
            print(f'{tran[0]:15s} {tran[1]:10.2f} {tran[2].strftime("%d/%m/%Y")}')

        print(f'saldo atual: {conta.saldo} \n')