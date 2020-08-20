var = float(input('Em qual velocidade o carro passou no radar? km/h: '))
multa = (var - 80) * 7
if var>80:
    print('Você foi multado em {:.2f} reais'.format(multa))