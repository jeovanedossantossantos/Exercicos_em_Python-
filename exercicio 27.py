#fibonacci
'''g=int(input())
ultimo=0
penultimo=0
atual=1
n=1
f=0
while n <= g:
    if n==1:
        
        print('0', end=' ')
            
   print(%i%atual, end=' ')
    if atual==0:
        atual=1
    penultimo = ultimo
    print('%i'%penultimo,end='')
    ultimo = atual
#    print('u ',ultimo)
    atual = ultimo + penultimo
#    print('a ',atual)
    n+=1'''
'''g=int(input())
ultimo=0
penultimo=0
atual=1
n=1
while n <= g:
    
    penultimo = ultimo
    print('%i'%penultimo,end='')
    ultimo = atual
    atual = ultimo + penultimo
    n+=1'''
'''k=int(input())
tempo= k * 2
print('%i minutos'%tempo)'''
'''dias=int(input())
ano= dias//365
anor= dias % 365
mes = anor // 30
mesr= anor % 30
dia=mesr

print('%i ano(s)\n%i mes(es)\n%i dia(s)'%(ano,mes,dia))'''

'''n=1
while n <= 100:
    if n % 2 ==0:
        print(n)
    n+=1'''
#a=float(input())
'''b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())'''
'''n=0
s=0
while n < 6:
    a=float(input())
    if a > 0:
        s+=1
    n+=1
print('%i valores positivos'%s)'''

'''n=1
x=int(input())
while n <= x:
    if n %2 != 0:
        print(n)
    n+=1'''

'''n=0
soma=0
d=0
while n < 6:
    a=float(input())
    if a > 0:
        soma=soma + a
        d+=1
    n+=1
soma=soma/d
print('%i valores positivos\n%.1f'%(d,soma))'''
'''n=0
s=0
while n < 5:
    a=int(input())
    if a % 2==0:
        s+=1
    n+=1
print('%i valores pares'%s)'''

'''todoido=input().split()
a=int(todoido[0])
b=int(todoido[1])
if b < a:
    c=b
    b=a
    a=c
if b%a==0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')'''
'''n=float(input())

if n <= 25 and n >= 0:
    print('Intervalo [0,25]')
elif n > 25 and n <= 50:
    print('Intervalo (25,50]')
elif n > 50 and n <= 75:
    print('Intervalo (50,75]')
elif n > 75 and n <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')'''
'''seg=int(input())
h=seg//3600
hr=seg%3600
m=hr//60
mr=hr%60
s=mr
print('%i:%i:%i'%(h,m,s))'''
'''k=int(input())
l=float(input())

kl = k/l
print('%.3f km/l'%kl)'''
'''tes=int(input())
a=0
while a < tes:
    te=int(input())

    an=1*2**(te - 1)
    sn=(1*(2**te)-1)
    print(an)
    print(sn)'''
'''g=int(input())
ultimo=0
penultimo=0
atual=1
n=1
resultado = ''
while n <= g:
    penultimo = ultimo
    resultado += str(penultimo) + ' '
    ultimo = atual
    atual = ultimo + penultimo
    n+=1
print(resultado[:-1],end='')
print()'''



n=input()

while n != 'EOF':
    if n == '0':
        print('vai ter copa!')
    else:
        print('vai ter duas!')
    n=input()


    

            

