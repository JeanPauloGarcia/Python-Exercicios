n = float(input('Qual será a distância percorrida? km: '))
if n<200:
    n1 = n * 0.5
    print('O preço da viagem será: R${:.2f}'.format(n1))
else:
    n2 = n * 0.45
    print('O preço da viagem será: R${:.2f}'.format(n2))
