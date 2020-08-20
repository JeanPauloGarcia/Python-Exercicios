import random
from time import sleep
n = random.randint(0,5) # escolha do número
print('-=-'*20)
print('Escolhendo um número de 0 a 5...')
print('-=-'*20)
n1 = int(input('Tente adivinhar qual foi o número escolhido: ')) # entrada do usuário
print('Processando...')
sleep(1)
if n1 == n: # condição acerto
    print('Você acertou! o número escolhido foi {}'.format(n))
else: # condição erro
    print('Você errou! O número escolhido foi {}'.format(n))