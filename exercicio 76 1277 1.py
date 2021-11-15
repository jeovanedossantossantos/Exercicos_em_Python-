n=int(input())
for i in range(n):
    nuemro_alunos=int(input())
    nomes_alunos=input().split()
    frequencia=input().split()
    lista=[]
    nomes=''
    s=0
    for j in range(len(nomes_alunos)):
        soma=0
        somap=0
        rep=0
       # print(frequencia[j])
        fre=str(frequencia[j])
#        print(frequencia)
        for t in range(len(frequencia[j])):
            b=str(fre[t])
            if b == 'A':
                soma=+1
            elif b == 'P':
                somap+=1
            elif b == 'M':
                rep-=1
            rep+=1
                #rep=100
                #A=X
                #100A=repx
                #x=100A/rep
        ra=(100 * soma)/rep
        rp=(100 * somap)/rep
       # print('ra',ra)
        #print('rp',rp)
        if rp < 75:
            lista.append(nomes_alunos[j])
    for j in range(len(lista)):
        print(lista)
        nomes += str(lista[j]) + ' '
    print(nomes[:-1])
        
