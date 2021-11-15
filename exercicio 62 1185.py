mat=[]
linha=[]
soma=0
st=input()
#c=1
#valor=0
for i in range(12):
    j=0
    for j in range(12):
        valor=float(input())
#        valor+=c
        linha.append(valor)
    mat.append(linha)
    linha=[]
n=11
div=0
for i in range(n):
    for j in range(n):
        b=float(mat[i][j])
        soma+=b
#        print(b,end=' ')
        div+=1
#    print()
    j=0
    n-=1
if st=='S':
    print('%.1f'%soma)
elif st=='M':
    soma=soma/div
    print('%.1f'%soma)
