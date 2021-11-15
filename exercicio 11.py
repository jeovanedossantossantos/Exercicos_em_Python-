#1.	Faça um Programa que peça dois números e imprima o maior deles..

a=int(input('Digite o primeiro numero\n'))
b=int(input('Digite o segundo numero\n'))

if a>b:
    print('{} é maior que {}'.format(a,b))
else:
    print('{} é maior que {}'.format(b,a))
