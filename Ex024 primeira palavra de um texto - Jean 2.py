name = input('Digite o nome de uma cidade: ')
var = name.upper().split()
print('O nome da cidade {} começa com "SANTO"?: {}'.format(name, 'SANTO' in var[0]))