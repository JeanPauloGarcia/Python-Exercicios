n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Agora mais um: '))
if n2-n3<n1<n2+n3 and n1-n3<n2<n1+n3 and n1-n2<n3<n1+n2:
    print('Os números podem formar um triângulo!')
else:
    print('Não forma um triângulo')