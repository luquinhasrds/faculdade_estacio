import cores as cor
#codigo da classe
class Conta:
    def __init__(self, numero, cpf, nome_titular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False # sem saldo o suficiente
        else:
            self.saldo -=valor
            return True

    def gerar_extrato(self):
        print(f'numero: {self.numero}\ncpf: {self.cpf}\nnome: {self.nome_titular}\nsaldo: {self.saldo}')

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente')
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            return('transferencia realizada com sucesso')

'''
#codigo da classe
c1 = Conta(1, 123456541, "Guanabara", 1000)
c1.depositar(5000)
valor_saque = 1000
if c1.sacar(valor_saque):
    print(f'{cor.VERDE}valor de saque: {valor_saque}, realizado com sucesso!{cor.RESET}')
else:
    print(f'{cor.VERMELHO}saldo insuficiente.{cor.RESET}')

c1.gerar_extrato()
'''

conta1 = Conta(123, 123123123,'maria', 0)
conta2 =  Conta(124, 234234234, 'pedro', 500)

print(conta1.transfere_valor(conta2, 500))