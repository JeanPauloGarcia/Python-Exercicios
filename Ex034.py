sal = float(input('Digite o salário: R$ '))
if sal >= 1250.00:
    print('Seu aumento foi de: R$', (sal*0.1)+sal)
else:
    print('Seu aumento foi de: R$', (sal*0.15)+sal)
