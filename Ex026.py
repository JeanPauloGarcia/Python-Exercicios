print("""Ler frase e mostrar:
1 - quantas vezes aparece a letra "A"
Em que posição ela aparece 
2 - na primeira vez
3 - na última vez""")
msg = input('Digite uma frase: ')
print('A letra "a" aparece {} vez(e)s'.format(msg.count('a')))
print('A letra "a" aparece pela primeira vez no campo {}'.format(msg.find('a')))
print('A letra "a" aparece pela última vez no campo', msg.rfind('a'))