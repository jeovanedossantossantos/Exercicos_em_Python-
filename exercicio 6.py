#6.	Faça um programa para uma loja de tintas. O programa deverá
#pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros
#quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o
#preço total.

'''from math import *

m=float(input('Qual a area em metros quadrados que ser pintada\n'))
#n=float(input('Quantos litros voce vai precisa\n'))

# 1 = 3
# L = M M=3L  L=M/3
# LATAS = L/18
# PREÇÕ = LATAS*80

l=m/3
#l= math.floor(l)

#lr=m%3
#if(lr<= 3):

 #   lr= math.hceil(lr)

#else:

    #lr= math.floar(lr)

#ml=l+lr
latas=l/18
latas= ceil(latas)
preco=latas*80


print('A quantidade de latas necessaria é:\n',latas)
print('O preçõ a ser gasto sera de:\n',preco)'''
'''from math import *

numrep=int(input())
for varia in range(numrep):
    popu=input().split()
    pa=int(popu[0])
    pb=int(popu[1])
    g1=float(popu[2])
    g2=float(popu[3])
    
    if g1 < g2:
        break
    contb=0
    g1= g1/100
    g2= g2/100
        
    while pa <= pb:

        soma0 = pa * g1
        soma0=floor(soma0)
#        print(soma0)
        pa=pa+soma0
        pa=floor(pa)
#        print(pa)
        soma2=pb * g2
        pb=pb+soma2
        contb=contb + 1
        
    if contb > 100:
        print('Mais de 1 seculo.')
    else:
        print('%i anos.'%contb)'''
from math import *

numrep=int(input())
'''popula=input().split()
pa=int(popula[0])
pb=int(popula[1])
g1=float(popula[2])
g2=float(popula[3])'''
v=0
#for varia in range(numrep):
while v < numrep:
    popula=input().split()
    pa=int(popula[0])
    pb=int(popula[1])
    g1=float(popula[2])
    g2=float(popula[3])
    if g1 < g2:
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
    v+=1
'''    popula=input().split()
    pa=int(popula[0])
    pb=int(popula[1])
    g1=float(popula[2])
    g2=float(popula[3])'''
#v+=1
