from Classes.Conta import Conta
from Classes.Poupanca import Poupanca

class ContaRemunerada(Conta, Poupanca):
    def __init__(self, clientes, numero, saldo, taxa_remuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)


    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)