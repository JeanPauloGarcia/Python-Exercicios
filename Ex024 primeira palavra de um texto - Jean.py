print('Ler nome de cidade e dizer se começa com o nome "SANTO"')
nome = input('Digite um nome de cidade: ')
var = nome.split()
print('o primeiro nome é "Santo" em {}?: {} ({})'.format(nome, 'Santo' in var[0], var[0].find('Santo')))

