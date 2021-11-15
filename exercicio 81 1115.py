ponto=input().split()
x=int(ponto[0])
y=int(ponto[1])
while x != 0 or y != 0:
    if x == 0 or y ==0:
        break
    if x > 0 and y > 0:
        print('primeiro')
    elif x > 0 and y < 0:
        print('quarto')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x < 0 and y > 0:
        print('segundo')
    ponto=input().split()
    x=int(ponto[0])
    y=int(ponto[1])
