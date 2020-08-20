print('Ler um nome de pessoa e dizer se tem "SILVA" no nome')
msg = input('Digite um nome completo: ')
print('Em "{}" possui o nome Silva?: {}'.format(msg, 'Silva' in msg))