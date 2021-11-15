x=int(input())
y=int(input())

if x > y:
    v=x
    x=y
    y=v
while x < y-1:
    x+=1
    r=x%5
    if r==2 or r==3:
        print(x)
