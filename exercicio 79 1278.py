import re
n=1
while n != 0:
    n=int(input())
    vetor=[]
    mat=[]
    if n == 0:
        break
    else:
        for i in range(n):
            palavra=input()
            branco=list(set(palavra))
            bra=ord(branco[0])
            if bra == 32:
                palavra=''
                n-=1
            else:
                vetor.append(palavra)
            b=''
        for i in range(n):
            b=str(vetor[i])
            b=re.sub('\s+', ' ', b)
            b=b.strip()
            mat.append(b)
        #DESCOBRINDO O MAIOR TERMO E VER A DIFERENÇA ENTRE O MAIOR E O MENO]
            maior=0
            gaz=[]
        for i in range(len(mat)):
            menor = len(mat[i])
            gaz.append(menor)
            maior=max(gaz)
            menor=min(gaz)

        var=''
        jeovane=[]
        for i in range(n):
            santos=[]
            for j in range(maior):
                santos.append(' ')
            jeovane.append(santos)
        for i in range(n):
            meno=len(mat[i])
            if i == 0:
                soma = maior - menor
            matriz=list(mat[i])
            for j in range(len(matriz)):
                jeovane[i][j]=str(matriz[j])
        for i in range(n):
            stry=''
            for j in range(len(jeovane[0])):
                stry+=str(jeovane[i][j])
            stry=stry.strip()
            p=len(jeovane[0]) - len(stry)
            g=len(stry)
            if len(stry) != len(jeovane[0]):
                stry=stry.rjust(p+g)
            print(stry)
    print()
