while True:
    n=input().split()
    x=int(n[0])
    y=int(n[1])
    if x <= 0 or y <= 0:
        break
    else:
        if y < x:
            z=x
            x=y
            y=z
        di=y-x
        soma=''
        soma2=0
        for j in range(di+1):
            soma2+=x
            soma+=str(x)+' '
            x+=1
        soma+='Sum=' +str(soma2)
        print(soma)
