'''Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
de modo que o lado A representa o maior dos 3 lados. A seguir,
determine o tipo de triângulo que estes três lados formam, com base
nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) ,
B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.'''
'''for n in range(10000):
    valor=input().split()

    a=float(valor[0])
    b=float(valor[1])
    c=float(valor[2])

    d=a
    e=b
    f=c
    if a > 0 and b > 0 and c > 0:
        if a > b and a > c and b > c:
            a=a
            b=b
            c=c
            print(a,b,c)
        elif a < b and a > c and b > c:
            a=b
            b=d
            print(a,b,c)
        elif a < b and a < c and b > c:
            a=b
            b=c
            c=d
            print(a,b,c)
        elif a < b and a < c and b < c:
            a=c
            c=d
            print(a,b,c)
        elif a==b and a < c > b:

            a=c
            c=b
            print(a,b,c)
        elif c>a< b and c==b:
            a=c
            c=d
            print(a,b,c)
        elif a==b and a>c<b:
            a=a
            b=b
            c=c
            print(a,b,c)
        else:
            b = c
            c = e
            print(a,b,c)
        if a >= (b+c): #or a != b and b != c and a != c:
            print('NAO FORMA TRIANGULO')
        elif a**2 == (b**2 + c**2):
            print('TRIANGULO RETANGULO')
        elif a**2 > (b**2 + c**2):
            print('TRIANGULO OBTUSANGULO')
        elif a**2 < (b**2 + c**2):
            print('TRIANGULO ACUTANGULO')
        if a==b and b==c and a==c:
            print('TRIANGULO EQUILATERO')
        elif a < (b+c) and (False == (a != b and b != c and a != c)):
        
            print('TRIANGULO ISOSCELES')
    else:
        print('NAO FORMA TRIANGULO')'''
valor=input().split()
a=float(valor[0])
b=float(valor[1])
c=float(valor[2])
d=a
e=b
f=c
if a < b and c < b and a < c:
    
    a=b
    b=c
    c=d
#    print(a,b,c)
elif a > b and c > b and a > c:
    c=b
    b=f
#    print(a,b,c)
elif a==b and a > c:
    a=a
    b=b
    c=c
#    print(a,b,c)
elif a > b and a==c:
    a=a
    b=c
    c=e
#    print(a,b,c)
elif a == b and a < c:
    a=c
    c=b
#    print(a,b,c)
elif a < b and a == c:

    a=b
    b=c
#    print(a,b,c)
elif b > a and b > c and c < a:
    a=b
    b=d
#    print(a,b,c)
elif b < a and b < c and a > c:
    c=b
    b=f
#    print(a,b,c)
elif c > b and c > a and a > b:
    a=c
    c=b
    b=d
#    print(a,b,c)
elif b==c and a > b:
    a=a
    b=c
#    print(a,b,c)
elif c>a and c>b and a < b:
    a=c
    c=d
#    print(a,b,c)
else:
    b=c
    c=e
#print(a,b,c)

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2 + c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2 + c**2):
    print('TRIANGULO ACUTANGULO')
if a==b and b==c and a==c:
    print('TRIANGULO EQUILATERO')
elif a < (b+c) and (False == (a != b and b != c and a != c)):    
    print('TRIANGULO ISOSCELES')
