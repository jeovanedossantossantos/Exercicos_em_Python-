#4.	Faça um Programa que leia três números e mostre o maior e o menor deles.

numero=input('Digite tres numeros\n').split()

a=float(numero[0])
b=float(numero[1])
c=float(numero[2])

if a>b and a>c:
    print('{} é o maior numero'.format(a))
elif b>c:
    print('{} é o maior número'.format(b))
else:
    print('{} é o maior número'.format(c))
