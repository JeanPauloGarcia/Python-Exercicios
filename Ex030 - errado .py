n = str(input('Digite um número inteiro: ')).split()
n1 = n[0][-1]
if n1 == '0' or '2' or '4' or '6' or '8':
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÌMPAR'.format(n))