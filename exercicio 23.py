'''Leia 3 valores inteiros e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente, uma linha em
branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.'''
'''valor=input().split()

a=int(valor[0])
b=int(valor[1])
c=int(valor[2])

d=a#se b fosse eu ia dar o valor de b a 
e=b
f=c

if a > b and a > c and b > c:
   a=c
   c=d
   
   print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
elif a > b and c > b and a > c:
    a=b
    b=c
    c=d
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
elif b > a and c > a and b > c:
    b=c
    c=e
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))

elif b > c and c < a and a < b:
    a=c
    c=b
    b=d
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
elif c > a and a > b and b < c:
    b=a
    a=e
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
else:
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
'''
valor=input().split()

a=int(valor[0])
b=int(valor[1])
c=int(valor[2])

d=a#se b fosse eu ia dar o valor de b a 
e=b
f=c

if a > b and a > c and b > c:
   a=c
   c=d
   
   print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
elif a > b and c > b and a > c:
    a=b
    b=c
    c=d
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
elif b > a and c > a and b > c:
    b=c
    c=e
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))

elif b > c and c < a and a < b:
    a=c
    c=b
    b=d
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
elif c > a and a > b and b < c:
    b=a
    a=e
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))
else:
    print('%i\n%i\n%i\n\n%i\n%i\n%i'%(a,b,c,d,e,f))

