from classes.Cliente import Cliente
from classes.Conta import Conta

#testando o código
cliente1 = Cliente('123123123', 'Joao', 'Rua xis')
cliente2 = Cliente('2224224224', 'maria', 'Rua 2 xises')
cliente3 = Cliente('789789789', 'lucas', 'Rua 3 dogs')
cliente4 = Cliente('456456456', 'duda', 'Rua alelozinho0')

conta1 = Conta([cliente1, cliente2], 111, 0)
conta2 = Conta([cliente3, cliente4], 150, 5000)

#CONTA1
'''
conta1.gerar_saldo()
conta1.depositar(1000)
conta1.gerar_saldo()
conta1.sacar(2000)
conta1.gerar_saldo()

#CONTA2
conta2.gerar_saldo()
conta2.dados_cliente()
'''

conta1.depositar(2000)
conta1.sacar(500)

conta1.extrato.gerar_extrato(conta1.numero)