print('{}'.format(' Triângulos '))
n1 = int(input('{}'.format('1ª reta: ')))
n2 = int(input('{}'.format('2ª reta: ')))
n3 = int(input('{}'.format('3ª reta: ')))
# Condição de Existência
if n2 + n3 > n1 and n2 + n1 > n3 and n3 + n1 > n2:
    print('triangulo:')
    # GUAN     print('triangulo:', =end'')
    # tipos de triângulo
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('Escaleno')
    # GUAN elif n1 != n2 != n3 != n1:
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Isósceletes')
    #GUAN else:
        #GUAN print('Isósceles')
else:
    print('Não forma um triangulo')