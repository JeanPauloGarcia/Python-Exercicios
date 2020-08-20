#Modo 1
km = float(input('Quantos km rodados?: '))
d = float(input('Quantos dias alugados?: '))
custo1 = km * 0.15
custo2 = d * 60
print('O valor a pagar do aluguel do carro por {} dias e {} quilômetros é {:.2f}R$'.format(d, km, custo1 + custo2))
#Modo 2
dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos Km rodados?: '))
pago = (dias * 60) + (0.15 * km)
print('O total a pagar é: R$ {:.2f}'.format(pago))
