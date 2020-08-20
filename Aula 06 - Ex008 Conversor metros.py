print('{:=^90}'.format(' Desafio 008 '))
print('{:=^90}'.format(' Escrevendo um valor em metros e convertendo em centímetros e milímetros '))
print('='*90)
n = float(input('Metros: '))
print('{} metro(s): \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm '.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))
#km. hm. dam. m. dm. cm. mm.


