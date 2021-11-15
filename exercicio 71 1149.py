valor=input().split()
a=int(valor[0])
n=int(valor[1])
while n <= 0:
    n=int(input())
c=0
while c<=a+1:
    b=a+c
    c+=1
print(b)
