nasc = int(input('Nascimento: '))
import datetime
ano = datetime.date.today().year
idade = ano - nasc
print('{} anos'.format(idade))
if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
else:
    print('OUTRO')
