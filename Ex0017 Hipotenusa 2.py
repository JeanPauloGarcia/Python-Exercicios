from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(ca, co)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))

