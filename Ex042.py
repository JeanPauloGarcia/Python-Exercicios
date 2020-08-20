
n1 = int(input('Primeiro númeoro: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
if n1>(n2+n3) or n2>(n1+n3) or n3>(n2+n3):
    print('Não é um triângulo')
elif n1==n2==n3:
    print('Equilatero')
elif n1==n2 or n1==n3:
    print('Isósceles')
elif n1!=n2!=n3:
    print('Escaleno')


