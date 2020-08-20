
msg = ("Ex027 - Ler nome completo de pessoa e mostrar o primeiro e o último nome separadamente.")
print(msg)
print('{:^87}'.format('A contagem é de: {} caracteres'.format(len(msg))))
print('-'*87)
nome = input('Digite um nome completo: ')
var = nome.split()
print('primeiro: ', var[0])
print('último: ', var[2])