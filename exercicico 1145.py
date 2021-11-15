valor = input().split()

colunas = int(valor[0])
termos = int(valor[1])
cont = 0
linha=''
contlin = 0
while cont < termos:
    cont+=1
    if contlin < (colunas - 1):
        linha+=str(cont) + ' '
        contlin += 1
    elif cont < (termos -1):
        linha+=str(cont) + '\n'
        contlin=0
    else:
        linha+=str(cont)
print(linha)
