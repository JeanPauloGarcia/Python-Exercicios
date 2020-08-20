from math import cos,tan, sin, radians
ang = int(input('Digite um ângulo: °'))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('Seno: {:.2f}, \nCosseno: {:.2f} e \nTangente: {:.2f}.'.format(s, c, t))
