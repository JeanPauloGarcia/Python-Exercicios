print('\033[34m NATAÇÃO \033[m')
n1 = int(input('\033[31mano de nascimento: '))
import datetime
c = datetime.date.today().year - n1
print(c)
if c <= 9:
    v = 'MIRIM'
elif 9 < c <= 14:
    v = 'INFANTIL'
elif 14 < c <= 19:
    v = 'JUNIOR'
elif 19 < c <= 20:
    v = 'SÊNIOR'
else:
    v = 'MASTER'
print('\033[34mO atleta é da categoria {}'.format(v))

