nome = input('Digite um nome completo: ')
print('A letra "a" aparece {} vezes'.format(nome.lower().count('a')))
print('A letra "a" aparece pela primeira vez no caractere {}'.format(nome.lower().find('a')))
print('A letra "a" aparece pela última vez no caractere {}'.format(nome.lower().rfind('a')))