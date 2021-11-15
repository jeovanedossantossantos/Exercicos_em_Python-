n=1
while n != 0:
    nu=1
    n=int(input())
    mat=[]
    if n == 0:
        break
    else:
        for i in range(n):
            linha=[]
            soma=''
            for j in range(n):
                linha.append(nu)
                nu=nu*2
    #pegar o ultimo termo da matriz
            mat.append(linha)
            if len(linha) > 1:
                nu=int(mat[i][1])
        if n <= 2:
            b=1
            for i in range(n):
                li=''
                for j in range(n):
                    li+='{:>1}'.format(mat[i][j]) + ' '
                print(li[:-1])
            print()
        else:
            ultimo = int(mat[n-1][n-1])
            ultimo=len(str(ultimo))
            for i in range(n):
                li=''
                for j in range(n):
                    valorinicial=len(str(mat[i][j]))
                    stry=str(mat[i][j])
                    diferenca = ultimo - valorinicial
                   # if diferenca == 0:
                    #    li+=' '
                    for k in range(diferenca):
                        li+=' '
                    li+=str(mat[i][j])+' '
                print(li[:-1])
            print()
'''    else:
        for i in range(n):
            li=''
            for j in range(n):
                li+='{:>3}'.format(mat[i][j]) + ' '
            print(li[:-1])'''
        
        
            
'''
while True:
    n = int(input())
    
    if n == 0:
        break
    
    matriz = [ \
              [0 for elemento in range(n)]
                  for linha in range(n)
    ]
    
    indice = 0
    numero = 1
    
    while indice < n:
        for i in range(n):
            if i >= indice:
                matriz[indice][i] = numero
                matriz[i][indice] = numero
        indice += 1
        numero += 1
    
    offset = n - 1
    
    for i in range(n):
        for j in range(n):
            matriz[offset-j][offset-i] = matriz[i][j]
    
    for i in range(n):
        linha = ''
        for j in range(n):
            linha += '{:>3}'.format(str(matriz[i][j])) + ' '
        print(linha[:-1])
    print()'''
        



