n=int(input())
for i in range(n):
    valor=input().split()
    x=int(valor[0])
    y=int(valor[1])
    if y != 0:
        d=(x/y)
        print(d)
    else:
        print('divisao impossivel')
