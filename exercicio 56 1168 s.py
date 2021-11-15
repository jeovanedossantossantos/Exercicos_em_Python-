'''n=int(input())
for i in range(n):
    leds=0
    valor=input()
    strig=list(valor)
    rep=len(strig)
    r=0
    for r in range(rep):
        strig[r]=int(strig[r])
        if strig[r] == 0:
            leds+=6
        elif strig[r] == 1:
            leds+=2
        elif strig[r] == 2:
            leds+=5
        elif strig[r] == 3:
            leds+=5
        elif strig[r] == 4:
            leds+=4
        elif strig[r] == 5:
            leds+=5
        elif strig[r] == 6:
            leds+=6
        elif strig[r] == 7:
            leds+=3
        elif strig[r] == 8:
            leds+=7
        elif strig[r] == 9:
            leds+=6
    print('{} leds'.format(leds))'''
repe=int(input())
mapa=[6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range(repe):
    leds=input()
    soma=0
    for led in leds:
        print(led)
        numero=int(led)
        soma += mapa[numero]
    print(soma,'leds')
