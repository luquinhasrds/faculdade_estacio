from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.ContaEspecial import ContaEspecial

cliente1 = Cliente('lucas', '123', 'rua 1')
cliente2 = Cliente('maria', '456', 'rua 2')
cliente3 = Cliente('joao', '789', 'rua 3')

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 2000, 1000)

conta1.depositar(300)
conta1.tranfere_valor(conta2, 500)

conta2.sacar(1500)

conta3.depositar(800)

conta1.extrato.gerar_extrato(conta1)
conta2.extrato.gerar_extrato(conta2)
conta3.extrato.gerar_extrato(conta3)