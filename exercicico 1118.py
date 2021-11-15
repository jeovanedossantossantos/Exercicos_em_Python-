while True:
    cont=0
    soma = 0
    while cont < 2:   
        n = float(input())
        if n >= 0 and n <= 10:
            soma = soma + n
            cont = cont +1
        else:
            print("nota invalida")
    print("media = %.2f"%(soma/2))
    r = int(input("novo calculo (1-sim 2-nao)"))
    while r != 1 and r != 2:
        r = int(input("novo calculo (1-sim 2-nao)"))
    if r == 2:
        break
