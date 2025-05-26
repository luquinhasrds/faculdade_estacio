import datetime
from Classes.Extrato import Extrato


class Conta:

    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(['Deposito', valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Nao existe saldo suficiente da conta {self.numero} do cliente {self.clientes.cpf}')
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['Saque', valor, datetime.datetime.today()])
            return True

    def tranfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            print('nao existe saldo suficiente')
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(['Transferencia', valor, datetime.datetime.today()])
            return 'tranferencia realizada'

    def gerar_saldo(self):
        print(f'Conta: {self.numero}\nSaldo: R${self.saldo}:10.2f')