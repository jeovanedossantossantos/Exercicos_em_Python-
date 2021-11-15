#5.	Elabore um programa que receba três valores digitados A, B e C e
#informe se estes podem ou não ser os lados de um triângulo.
#ABC é triângulo somente se
#A < B + C E
#B < A + C E
#C < A + B.

a=float(input('Digite o 1° número\n'))
b=float(input('Digite o 2° número\n'))
c=float(input('Digite o 3° número\n'))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('Sim podem ser lados de um triângulo\n')
else:
    print('Não podem ser lados de um triângulo\n')
