carro = int(input('Qual foi a velocidade do carro?: '))
calculo = (carro-80) * 7
if carro > 80:
    print('Você foi multado em {} reais'.format(calculo))
else:
    print('Você está dentro do limite de velocidade')
print('Tenha um bom dia! Dirija com segurança!')