n = float(input('Distância viagem: '))
'''if n > 200:
    n1 = n*0.45
else:
    n1 = n*0.5'''
# modo 2
n1 = n*0.5 if n<=200 else n*0.45
print('Sua viagem de {}km custará {} reais'.format(n, n1))

