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
div=0

i=1
n=11
v=1
for j in range(6):
    while i < n:
        b=float(mat[i][j])
#        print(b,end=' ')
        soma+=b
        div+=1
        i+=1
#    print()
    v+=1
    i=v
    n-=1
if st=='S':
    print('%.1f'%soma)
elif st=='M':
    soma=soma/div
    print('%.1f'%soma)
