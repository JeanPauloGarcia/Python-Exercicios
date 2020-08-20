s = 0
for c in range(1,7):
    n = int(input('Digite um nº: '))
    if n % 2 == 0:
        s+=n
print('Soma dos números pares: {}'.format(s))
