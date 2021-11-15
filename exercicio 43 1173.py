vetor=[]
n=int(input())
v=0
i=0
while v < 10: 
   vetor.append(n)
   print('N[%i] = %i'%(v,vetor[i]))
   n=n*2
   i+=1
   v+=1
