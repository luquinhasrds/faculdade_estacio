from classes import cores
import datetime

class Conta:

    __total_conta = 0

    @classmethod
    def get_total_contas(cls):
        return cls.__total_conta
    
    @staticmethod
    def nome_banco():
        return 'Banco guanabara'

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        type(self).__total_conta += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print('Saldo invalido!')
        else:
            self.__saldo = valor

    def sacar(self, valor):
        if self.__saldo < valor:
            return False # sem saldo o suficiente
        else:
            self.__saldo -=valor
            return True

    def gerar_saldo(self):
        print(f'Conta: {self.__numero}')
        print(f'Saldo: R${self.__saldo:10.2f}')