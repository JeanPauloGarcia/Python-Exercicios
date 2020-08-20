n = int(input('Ano de nascimento: '))
import datetime
ano = datetime.date.today().year
idade = ano - n
v2 = 18 - idade
v3 = idade - 18
print('Em {} quem nasceu em {} tem {} anos'.format(ano, n, idade))
sexo = str(input('Sexo: ')).strip().upper()
if sexo == 'MASCULINO':
    print('Alistamento obrigatório!')
    if idade < 18:
        print('Ainda faltam {} ano(s) para o alistamento'.format(v2))
        print('Seu alistamento deverá ser em {}'.format(ano + v2))
    elif idade == 18:
        print('Ano do alistamento!')
    elif idade > 18:
        print('Você deveria ter se alistado há {} ano(s)'.format(v3))
        print('Seu alistamento foi em {}'.format(ano - v3))
elif sexo == 'FEMININO':
    print('O alistamento ainda não é obrigatório para o sexo', sexo)
else:
    print('Por favor, preencha o campo Sexo com as palavras "masculino" ou "feminino"')

