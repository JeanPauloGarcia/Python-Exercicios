from datetime import date
n = int(input('Digite um ano ou "0" para analisar o ano atual: '))
if n == 0:
    print(date.today().year)
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('ano {} é bissexto!'.format(n))
else:
    print('ano {} é bissexto!'.format(n))