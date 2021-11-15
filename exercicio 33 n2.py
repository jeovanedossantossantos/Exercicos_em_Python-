#Dadas as informações de população e a taxa de crescimento de duas cidades:
#quantos anos levará para que a cidade menor (sempre é a cidade A) ultrapasse
#a cidade B em população.
'''cuja taxa de crescimento da cidade A é maior do que a taxa de crescimento
da cidade B, portanto, previamente já separou para você apenas os casos de
teste que tem a taxa de crescimento maior para a cidade A.'''
#Sua tarefa é construir um programa que apresente o tempo em anos
#para cada caso de teste.
#from math import *
'''numrep=int(input())
for varia in range(numrep):
    popu=(input()).split()
    pa=int(popu[0])
    pb=int(popu[1])
    g1=float(popu[2])
    g2=float(popu[3])
    conta=0
    if g1 < g2:
        break
    else:
        contb=0
        g1= g1/100
        g2= g2/100
        while pa <= pb:

            soma0= pa * g1
            pa=pa+soma0
            
            soma2=pb * g2
            pb=pb+soma2
            
            contb=contb + 1
        if contb > 100:
            print('Mais de 1 seculo.')
        else:
            print(contb, ' anos.')'''
'''a=100
b=150
v=0
while a <= b:
	c=a*0.01
	a=a+c
	a= floor(a)
	v=v+1
print(v)'''

#from math import *
'''
numrep=int(input())
popula=input().split()
pa=int(popula[0])
pb=int(popula[1])
g1=float(popula[2])
g2=float(popula[3])
for varia in range(numrep):
v=0
while v < numrep:
    popula=input().split()
    pa=int(popula[0])
    pb=int(popula[1])
    g1=float(popula[2])
    g2=float(popula[3])
    if g1 < g2:
        break
    if pa > pb:
        break
    contb=0
    g1 = g1/100
    g2 = g2/100    
    while pa <= pb:
        soma0 = pa * g1
        soma0=floor(soma0)
        pa=pa+soma0
        pa=floor(pa)
        soma2=pb * g2
        pb=pb+soma2
        contb=contb + 1    
    if contb > 100:
        print('Mais de 1 seculo.')
    else:
        print('%i anos.'%contb)
    v+=1'''
#from math import *

numrep=int(input())

for v in range(numrep):
    popula=input().split()
    pa=int(popula[0])
    pb=int(popula[1])
    g1=float(popula[2])
    g2=float(popula[3])
    contb=0
    g1 = g1/100
    g2 = g2/100    
    while pa <= pb:
        soma0 = pa * g1
        soma0=int(soma0)
        pa=pa+soma0
        
        
        soma2=pb * g2
        soma2= int(soma2)
        pb=pb+soma2
        contb=contb + 1
        
        if contb > 100:
            print('Mais de 1 seculo.')
            break
    if contb <= 100:
        print(contb,"anos.")
    
    
    
        
    
    
    
    
