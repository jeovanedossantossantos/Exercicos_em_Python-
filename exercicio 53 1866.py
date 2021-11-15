n=int(input())
for i in range(n):
    m=int(input())
    soma=0
    for j in range(m):
        if soma==0:
            soma=soma+1
        else:
            soma=soma-1
    print(soma)
