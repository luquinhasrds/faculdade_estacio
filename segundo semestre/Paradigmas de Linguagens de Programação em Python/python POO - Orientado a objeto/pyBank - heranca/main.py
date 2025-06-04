from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.ContaEspecial import ContaEspecial
from Classes.ContaRemunerada import ContaRemunerada

cliente1 = Cliente('lucas', '123', 'rua 1')
cliente2 = Cliente('maria', '456', 'rua 2')
cliente3 = Cliente('joao', '789', 'rua 3')

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaRemunerada(cliente3, 3, 2000, 0.5)

conta2.depositar(800)
conta2.gerar_saldo()

conta3.remuneraConta()
conta3.gerar_saldo()
