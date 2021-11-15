n=1
while n!=0:
    n=int(input())
    rep=1
    mat=[]
    for i in range(n):
        linha=[]
        c=1
        for j in range(n):
           linha.append(c)
        mat.append(linha)
    for i in range(n):
        d=rep
        for j in range(n):
            if i == j:
                mat[i][j]=1
                d=1
            elif i < j:
                mat[i][j]=d
            elif i > j:
                mat[i][j]=d
                d-=2
            d+=1
        rep+=1
    for i in range(n):
        soma=''
        for j in range(n):
           soma+='{:>3}'.format(str(mat[i][j])) + ' '
        print(soma[:-1])
    print()
