vetor=[]
t=0
i=0
for t in range(10):
    valor=int(input())
    vetor.append(valor)
    i+=1
i=0
for i in range(len(vetor)):
    n=int(vetor[i])
    if n <= 0:
        vetor[i]=1

    print('X[%i] = %i'%(i,vetor[i]))
    
    

