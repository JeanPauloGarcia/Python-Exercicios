#Zen of Python
'''import this'''
# Olá mundo
'''print('Olá mundo!')'''
#Concatenação
'''print('Olá', 5)'''
# Variável - Olá mundo
'''msg = ('Olá mundo!')
print(msg)'''
# Desafio 001 - Qual o seu nome
'''nome = input('Qual é o seu nome?: ')
print('Olá', nome, ', seja bem vindo!')'''
# Saída formatada {} - Qual o seu nome
'''nome = input('Digite o seu nome: ')
print('Olá {}, seja bem vindo!'.format(nome))'''
# Exibir informações na tela
'''nome = input('Qual o seu nome?: ')
idade = input('Quantos anos você tem?: ')
peso = input('Qual o seu peso?: ')
print(nome, idade, peso)'''
# Desafio 02 - data nascimento
'''dia = input('Dia do nascimento: ')
mes = input('Mês do nascimento: ')
ano = input('Ano do nascimento: ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')'''
# Concateção de 2 números
'''num1 = input('Digite um número: ')
num2 = input('Agora outro: ')
print('A soma entre', num1, 'e', num2, 'é:', num1+num2)'''
# Desafio 003 - Soma entre dois números - variáveis
'''var1 = int(input('Número: '))
var2 = int(input('Outro número: '))
soma = var1+var2
print('Soma:', soma)'''
# Dissecar - .isalgo
'''var = input('Digite algo: ')
print('O tipo primitivo é: ', type(var))
print('É só espaço?: ', var.isspace())
print('É só caixa baixa?:', var.islower())
print('Caixa alta?: ', var.isupper())
print('É numérico?: ', var.isnumeric())
print('É alfabétio?: ', var.isalpha())
print('É alfanumérico?: ', var.isalnum())
print('É capitalizado?: ', var.istitle())'''
# Casas decimais
'''var = float(input('Digite um número: '))'''
'''print('Float: {}, Int: {:.0f}'.format(var, var))'''
'''print('Float: {}, Int: {}'.format(var, int(var)))'''
'''s: float = 5 / 3
print(f"{s :.2f}")'''
# Sucessor e Antecessor
'''var = int(input("Digite um número: "))
s1 = var + 1
s2 = var - 1
print(f"O sucessor de {var} é {s1} e seu o antecessor é {s2}")'''
# Dobro, triplo, raiz
'''var = int(input('Digite um número: '))
d = var * 2
t = var * 3
r = var ** (1/2)
m = var / 2
inteira = var // 2
resto = var % 2
p2 = var ** 2
p3 = var ** 3
print(f"Dobro: {d} \ntriplo: {t}")
print(f"metade: {m} \nporção inteira: {inteira} \nresto da porção: {resto}")
print(f"raiz: {r} \npotência²: {p2} \npotência³: {p3}")'''
# Média da nota
'''n = int(input('Preencha a primeira nota: '))
n2 = int(input('Agora a segunda: '))
s = (n + n2) / 2
print(f'A média entre {n} e {n2} é: {s:}')'''
# Conversor metros
'''print(f'{"CONVERSOR de MEDIDAS":-^30}')
a = float(input('Qual o valor em metros?: '))
print('Quilômetros (km): {:10} \nHectômetros (hm): {:10}'.format(a*1000, a*100))
print('Decâmetros (dam): {:10} \nMetros (m): {:10} \nDecímetros (dm): {:10}'.format(a*10, a, a/10))
print('Centímetros (cm): {:10} \nMilímetros (mm): {:10}'.format(a/100, a/1000))'''
# Tabuada
'''n = int(input('Digite um número inteiro: '))
print('Tabuada de', n)
print('1 x {:2} = {} \n2 x {:2} = {} \n3 x {:2} = {}'.format(n, n*1, n, n*2, n, n*3))
print('4 x {:2} = {} \n5 x {:2} = {} \n6 x {:2} = {}'.format(n, n*4, n, n*5, n, n*6))
print('7 x {:2} = {} \n8 x {:2} = {} \n9 x {:2} = {} \n10 x {} = {}'.format(n, n*7, n, n*8, n, n*9, n, n*10))'''
# Conversor Dólares
'''dinheiro = float(input('Quanto você tem na carteira agora?: R$ '))
calculo = dinheiro/2.87
print('R${} vale C${:.2f}'.format(dinheiro, calculo))'''
# Área tinta
# Área
'''n = float(input("Altura da parede: "))
n2 = float(input('Largura da parede: '))
area = float(n * n2)
print('Uma parede de {}m por {}m possui uma área de {:.2f}m²'.format(n, n2, area))
# Rendimento
marca = input('Qual é a marca da tinta?: ')
lts = float(input('Quantos litros tem na lata: '))
rendimento = float(input('Rendimento da lata: '))
rendimentometro = lts / rendimento
print('É necessário aproximadamente {:.2f}l de tinta {} para pintar 1(um) m²'.format(rendimentometro, marca))
qtd = rendimentometro * area
print('Você precisará de aproximadamente {:.2f} litros para pintar uma área de {:.2f}m²'.format(qtd, area))'''
#
