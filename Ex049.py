n = int(input('Digite um nº: '))
print('Tabuada de {}:'.format(n))
for c in range(0,11):
    d = n * c
    print('{} x {} = {}'.format(n,c,d))
