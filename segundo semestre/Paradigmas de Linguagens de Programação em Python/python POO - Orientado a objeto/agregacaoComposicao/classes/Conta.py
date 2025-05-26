import classes.cores as cor
import datetime
from classes.Extrato import Extrato


#codigo da classe
class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato(self)

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            print(f'{cor.VERMELHO}Saldo insuficiente para sacar{cor.RESET}')
            return False # sem saldo o suficiente
        else:
            self.saldo -=valor
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente')
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append([f"Tranferencia para {conta_destino}", valor, datetime.datetime.today()])
            return('transferencia realizada com sucesso')

    def gerar_saldo(self):
        print(f'numero: {self.numero}\nsaldo: {self.saldo}')

    def dados_cliente(self):
        for cliente in self.clientes:
            print(f'Nome: {cliente.nome}\nEndereço: {cliente.endereco}')