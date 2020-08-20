altura = float(input('Altura: '))
massa = float(input('Massa: '))
IMC = massa/altura**2
print('Seu IMC é {:.2f}'.format(IMC))
if IMC < 18.5:
    print('ABAIXO')
elif IMC < 25:
    print('IDEAL')
elif IMC < 30:
    print('SOBREPESO')
else:
    print('OBESIDADE MÓRBIDA')