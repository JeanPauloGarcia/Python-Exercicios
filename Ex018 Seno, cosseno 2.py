'''import math
ang = float(input('Digite o ângulo: '))
print('O seno é: {:.2f}'.format(math.sin(math.radians(ang))))
print('O cosseno é: {:.2f}'.format(math.cos(math.radians(ang))))
print('A tangente é: {:.2f}'.format(math.tan(math.radians(ang))))'''
from math import radians, cos, sin, tan
ang = float(input('Digite o ângulo: '))
print('O Seno é {:.2f}'.format(sin(radians(ang))))
print('O Cosseno é: {:.2f}'.format(tan(radians(ang))))
print('A Tangente é: {:.2f}'.format(tan(radians(ang))))


