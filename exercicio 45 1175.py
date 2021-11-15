'''vetor=[]
lista=[]
for i in range(20):
    n=int(input())
    vetor.append(n)
g=19
for t in range(20):
    lista=vetor[g]
    print('N[%i] = %i'%(t,vetor[g]))
    g-=1
'''
'''valores =  input () .split ()
#A, B, C, D = valores

A =  int (valores[0])
B =  int (valores[1])
C =  int (valores[2])
D =  int (valores[3])

if ((B > C and D > A) and (C + D > B + A) and (C >= 0  and D >= 0 ) and (A % 2  == 0 )):
    print ("Valores aceitos")
else :
    print ("Valores nao aceitos")'''
valores=input().split()

N1=float(valores[0])
N2=float(valores[1])
N3=float(valores[2])
N4=float(valores[3])

nota_exame =  0.0
MEDIA=((N1 * 2 ) + (N2 * 3 ) + (N3 * 4 ) + (N4 * 1 )) / 10

print ('Mídia: %.1f'%MEDIA )

if MEDIA  >=  7.0:
    print ("Aluno aprovado")

if MEDIA  <  5.0:
    print ("Aluno reprovado")

if MEDIA  >=  5.0 and  MEDIA  <=  6.9:
    print ("Aluno em exame")
    nota_exame =float(input())
    print ("Nota do exame: %.1f"%nota_exame)
    MEDIA=(MEDIA  + nota_exame) / 2
    
    if MEDIA  >=  5.0:
        print ("Aluno aprovado")
    else :
        print ("Aluno reprovado")
    print ('Media final: %.1f'%MEDIA )
