#divisores
n=int(input())
d=1
soma=0
while d < n:
    if n%d==0:
        print(d)
        soma=soma+d

        d+=1
        
    else:
        d+=1
   
print(soma)
