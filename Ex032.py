n = int(input('Digite um ano: '))
n1 = (n % 4) == 0
n2 = (n % 100) == 00
n3 = (n % 400) == 0
if n1 == True and n2 == False and n3 == False:
    print('Fevereiro do ano {} tem 29 dias!'.format(n))
else:
    print('O ano {} não é bissexto'.format(n))