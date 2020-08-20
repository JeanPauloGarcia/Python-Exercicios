n1 = int(input('Digite um número: '))
n2 = int(input('Agora outro: '))
n3 = int(input('Mais um: '))
#n1
if n1 > n2 and n3:
    print('O maior é: {}'.format(n1))
if n1 < n2 and n3:
    print('O menor é', n1)
#n2
if n2 > n1 and n3:
    print('O maior é: {}'.format(n2))
if n2 < n3 and n1:
    print('O menor é'.format(n2))
#n3
if n3 > n2 and n1:
    print('O maior é: {}'.format(n3))
if n3 < n2 and n1:
    print('O menor é:', n3)
