x=int(input())
z=0
p=0
n=x
while z <= x:
    z=int(input())
#    cont+=1
x=0
while z >= x:
#    if z > x and z > 0:
    x=x+n
    n+=1
    p+=1
'''    elif z > x and z < 0 and x < 0:
        x=x-n
        n+=1
        p+=1'''
print('%i'%p)
