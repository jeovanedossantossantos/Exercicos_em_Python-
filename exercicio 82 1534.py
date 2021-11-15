while True:
    try:
        n=int(input())
        conp=n-1
        matriz=[]
        for i in range(n):
            linha=[]
            for j in range(n):
                if conp == j:
                    linha.append(2)
                    conp-=1
                elif i == j:
                    linha.append(1)
                else:
                    linha.append(3)
            matriz.append(linha)
        soma=''
        rep=0
        for i in range(n):
            for j in range(n):
                soma+=str(matriz[i][j])
                rep+=1
            if rep != (n*n):
                soma+='\n'
        print(soma)
    except EOFError:
        break
