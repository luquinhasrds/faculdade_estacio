def notas(*n, sit = False):
    """
    ->funcao para analisar notas dos alunos
    
    :param n: adiciona as notas dos alunos (numero de notas infinito)
    :param sit: mostra a situacao dos alunos da turma (se quiser)
    :param return: retorna o dicionario com os dados dos alunos
    """
    r = dict()
    r['total'] = len(n)
    r['maior nota'] = max(n)
    r['menor nota'] = min(n)
    r['media da turma'] = sum(n)/len(n)
    if r['media da turma'] > 6:
        r['situacao'] = 'BOA'
    else:
        r['situação'] = 'RUIM'
    
    return r

rest = notas(2.4, 5, 7, 10, 1, sit=True)

#print(rest)

help(notas)