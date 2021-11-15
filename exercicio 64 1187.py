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

n=11
i=0
j=1
while i < n:
    while j < n:
        b=float(mat[i][j])
        soma+=b
#        print(b,end=' ')
        j+=1
        div+=1
#    print()
    n-=1
    i+=1
    j=i+1
if st=='S':
    print('%.1f'%soma)
elif st=='M':
    soma=soma/div
    print('%.1f'%soma)
