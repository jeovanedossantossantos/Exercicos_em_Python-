#fatorial
'''n=int(input())
soma=0
d=1
while d < n:
    if d==1:
        soma=n*(n-1)
       
    else:
        soma=soma*(n-d)
        
    d=d+1
    
print(soma)
'''
'''n=int(input())
soma=n*(n-1)
d=2
while d < n:
       
    soma=soma*(n-d)
        
    d=d+1
    
print(soma)'''
p=int(input())
u=0
pa=0
a=1
n=1
r = ''
while n <= p:
    pa = u
    r += str(pa) + ' '
    u = a
    a = u + pa
    n+=1
print(r[:-1],end='')
print()
