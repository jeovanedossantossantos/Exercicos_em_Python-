while True:
    n=input().split()
    x=int(n[0])
    y=int(n[1])
    if x == y:
        break
    else:
        if x > y:
            print('Decrescente')
        else:
            print('Crescente')
