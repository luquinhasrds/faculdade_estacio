from classes.ContaCliente import ContaCliente
from classes.Banco import Banco
from classes.ContaComum import ContaComum
from classes.ContaVip import ContaRemunerada

banco1 = Banco(999, 'teste')

conta_comum1 = ContaComum(2, 0.01, 0.1, 2000, 0.05)
conta_remunerada = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)


banco1.adiciona_conta(conta_comum1)
banco1.adiciona_conta(conta_remunerada)

banco1.calcula_rendimento_mensal()
banco1.imprime_saldo_contas()