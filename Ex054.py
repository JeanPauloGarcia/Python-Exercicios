s = 0
s1 = 0
for c in range(0,7):
    n = int(input('Digite o seu ano de nascimento: '))
    idade = 2019 - n
    if idade < 21:
        s+=1
    else:
        s1+=1

print('Maior: {}, Menor: {}'.format(s1, s))