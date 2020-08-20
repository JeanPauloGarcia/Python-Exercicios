'''print('Exercício Python #022 - Analisador de Textos')
nome = input('Digite um nome completo: ').strip()
print('maiúsculas: {}'.format(nome.upper()))
print('minúsculas: {}'.format(nome.lower()))
var = nome.split()
print('quantidade de letras: {}'.format(len(''.join(var))))
print('quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
print('primeiro nome: {}, e tem {} letras'.format(var[0], len(var[0])))
print('primeiro nome tem {} letras'.format(nome.find(' ')))'''
'''print('Exercício Python #024 - Verificando as primeiras letras de um texto')
cid = str(input('Digite uma cidade: ')).strip()
var = cid.split()
print("SANTO" in var[0].upper())
print(var[0].upper().find('SANTO'))
print(cid[:5].upper() == 'SANTO')'''
'''print('Exercício Python #025 - Procurando uma string dentro de outra')
nome = str(input('digite um nome completo: ')).strip()
print('existe "silva" em {}?:'.format('silva' in nome.lower()))'''
'''print('Exercício Python #026 - Primeira e última ocorrência de uma string')
algo = str(input('digite algo: ')).upper().strip()
print('quantas vezes aparece a letra "a": {}'.format(algo.count('A')))
print('aparece pela primeira vez na posição {}'.format(algo.find('A')+1))
print('e pela última vez na posição {}'.format(algo.rfind('A')+1))'''
print('Exercício Python #027 - Primeiro e último nome de uma pessoa')
nome = str(input('Digite um nome completo: ')).strip()
var = nome.split()
print('1º nome: {}'.format(var[0]))
print('último nome: {}'.format(var[0-1]))



