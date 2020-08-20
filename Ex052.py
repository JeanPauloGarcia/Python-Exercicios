for c in range(10):
    n = int(input('Digite um número: '))
    list = [1, 2, 3, 5, 7, 9]
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 and n%9!=0 or n in list:
        print('Primo')
