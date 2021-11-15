n=int(input())
for i in range(n):
    numero=int(input())
    soma=''
    if numero == 0:
        soma+='NULL'
    else:
        if numero % 2 == 0:
            soma+='EVEN'
            if numero > 0:
                soma+=' '+'POSITIVE'
            elif numero < 0:
                soma+=' '+'NEGATIVE'
        else:
            soma+='ODD'
            if numero > 0:
                soma+=' '+'POSITIVE'
            elif numero < 0:
                soma+=' '+'NEGATIVE'
    print(soma)
