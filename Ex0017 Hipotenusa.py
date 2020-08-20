from math import sqrt
print('Hipotenusa de um triângulo retângulo')
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
s = sqrt(co**2 + ca**2)
print('A hipotenusa é: {:.2f}'.format(s))
