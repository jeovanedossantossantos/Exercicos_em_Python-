vetor=[]
for i in range(100):
    n=float(input())
    vetor.append(n)
    if n <= 10:
       print('A[%i] = %.1f'%(i,vetor[i]))
