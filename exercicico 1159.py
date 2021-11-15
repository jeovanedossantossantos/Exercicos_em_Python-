while True:
    x = int(input())
    if x == 0:
        break
    soma=0
    for i in range(x,(x+10),1):
        if i % 2 == 0:
          soma+=i
    print(soma)
