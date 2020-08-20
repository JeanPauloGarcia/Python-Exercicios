sal = float(input('Digite o salário: R$ '))
if sal > 1250.00:
    novo = (sal*0.1)+sal
else:
    novo = (sal * 0.15) + sal
print('Seu salário foi para: R${}'.format(novo))
