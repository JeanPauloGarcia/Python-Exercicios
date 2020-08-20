print('\033[34mcomparação de 2 números\033[m')
n1 = int(input('\033[33mDigite um número: '))
n2 = int(input('Digite o segundo número: \033[m'))
if n1 > n2:
    print('\033[34m{} maior que {}'.format(n1, n2))
elif n2 > n1:
    print('\033[34m{} menor que {}'.format(n1, n2))
else:
    print('\033[31mOs dois números são iguais!\033[m')