soma=0
rep=0
while True:
    n=float(input())
    if n >= 0 and n <= 10:
        soma+=n
        rep+=1
        if rep == 2:
            soma=soma/2
            print('media = %.2f'%soma)
            break
    else:
        print('nota invalida')
