#Desafio010
#Cálculo de área de uma parede e quanto é necessário de tinta sendo que cada litro, pinta 2m²
n1 = float(input('Altura da parede: '))
n2 = float(input('Largura da parede: '))
a = n1*n2
t = a/2
print('Área de:', a, 'm².', end=' >> ')
print('É necessário', t, 'litro(s) de tinta para pintar a parede')
