import random
list = ['pedra', 'papel', 'tesoura']
computador = random.choice(list)

jogador = str(input('Escolha pedra, papel ou tesoura: '))
n = 'você perdeu'
if jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
    n = 'você ganhou'
if jogador == 'pedra' and computador == 'pedra' or jogador == 'papel' and computador == 'papel' or jogador == 'tesoura' and computador == 'tesoura':
    n = 'nós empatamos'
if jogador == 'tesoura' and computador == 'pedra' or jogador == 'pedra' and computador == 'papel' or jogador == 'papel' and computador == 'tesoura':
    n = 'você perdeu'
else:
    print('Digitou errado!')
print('Eu escolhi {} e você {}, {}!'.format(computador, jogador, n))


