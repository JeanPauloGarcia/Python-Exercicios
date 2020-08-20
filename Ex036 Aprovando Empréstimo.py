n1 = float(input('valor da casa: '))
n2 = float(input('Salário: '))
n3 = float(input('Quantos anos: '))

percentv1 = n2*0.3
meses = n3*12
mensalidv3 = n1 / meses

if mensalidv3 >= percentv1:
    print('Negado! Valor da parcela R$ {:.2f} excedente a 30% do salário'.format(mensalidv3))
else:
    print('Aprovado! sua parcela será de R${:.2f}'.format(mensalidv3))

