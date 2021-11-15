n=int(input())

for s in range(n):
    
    x=int(input())
    d=1
    soma=0
    while d < x:
        if x%d==0:
#            print(d)
            soma=soma+d

            d+=1
        else:
            d+=1
#print(soma)
    if soma==x:
        print('%i eh perfeito'%x)
    else:
        print('%i nao eh perfeito'%x)

    
    
