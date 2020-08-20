print('{:=^50}'.format('\033[31;1m Média \033[m'))
n1 = float(input('\033[34mDigite a 1ª nota: '))
n2 = float(input('2ª nota: '))
c = (n1 + n2)/2
if c < 5.0:
    print('\033[31;1mREPROVADO')
elif 5 < c < 6.9:
    print('\033[33;1mRECUPERAÇÂO!')
else:
    print('\033[34;1mAPROVADO!')

