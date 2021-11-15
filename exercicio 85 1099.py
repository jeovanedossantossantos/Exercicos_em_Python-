n=int(input())
for i in range(n):
    xy=input().split()
    x=int(xy[0])
    y=int(xy[1])

    if y < x:
        z=x
        x=y
        y=z
    diferenca = y - x
    soma=0
    for j in range(diferenca):
        x+=1
        if (x % 2 != 0) and (x != y):
            soma+=x
    print(soma)
