print('Desafio 04')
a = input('Digite algo: ')
print('Você digitou:', (a))
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?: ', a.isspace())
print('"{}" é alfabético?: '.format(a), a.isalpha())
print('"{}" é um número?: '.format(a), a.isnumeric())
print('"{}" é alfanumérico?: '.format(a), a.isalnum())
print('Está em maiúsculas?: ', a.isupper())
print('Está em minúsculas?: ', a.islower())
print('Está capitalizada?: ', a.istitle())




