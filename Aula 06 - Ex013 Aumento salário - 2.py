salario = float(input('Digite o seu salário: R$ '))
aumento = salario + (salario * 15 / 100)
print('O seu salário de R${:.2f} com aumento de 15% fica R${:.2f}'.format(salario, aumento))
