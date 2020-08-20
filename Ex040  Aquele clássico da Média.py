nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
#nota3 = float(input('3ª nota: '))
media = (nota1 + nota2)/2
print('Nota {:.1f}'.format(media))
if media < 6:
    print('REPROVADO!')
elif 6 <= media < 7:
    print('Recuperação!')
else:
    print('Aprovado!')