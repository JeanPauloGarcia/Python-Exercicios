import random
n = random.randint(0,6)
print('Escolhendo um número de 0 a 6...\n...\n...')
n1 = int(input('Tente adivinhar qual foi o número escolhido: '))
print('Processando...')
if n1 == n:
    print('Você acertou! o número escolhido foi {}'.format(n))
else:
    print('Você errou! O número escolhido foi {}'.format(n))