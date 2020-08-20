preço = float(input('Preço: '))
print('''Preencha a forma de pagamento com:
1 - p/ À VISTA
2 - p/ CARTÃO 1x
3 - p/ CARTÃO 2x
4 - p/ CARTÃO 3x ou mais
''')
pagto = str(input('Pagamento: ')).strip()
if pagto == '1':
    preço = preço*0.9
elif pagto == '2':
    preço = preço*0.95
elif pagto == '4':
    preço = preço*1.2
print(preço)

