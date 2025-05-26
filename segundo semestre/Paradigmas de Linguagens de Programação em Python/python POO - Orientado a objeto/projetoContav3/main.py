from classes.conta import Conta

c1 = Conta('1', 1000)
c2 = Conta('2', 50)
c3 = Conta('3', 10000)

c1.saldo = 8000

print(c1.saldo)
#print(c2.saldo)

#c1._Conta__saldo = -8000   #forma que nao se deve usar, mas é um jeito de manipular um atributo protegido ou metodos
#print(f'Conta 1 com R$ {c1.saldo}')
#print(f'conta 2 com R$ {c2.saldo}')

#c1.gerar_saldo()
#c2.gerar_saldo()
print(f'Total de contas: {Conta.get_total_contas()}')
print(f'Muito obrigado por ser cliente do {Conta.nome_banco()}')