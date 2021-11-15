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
n=1
cont=0
i=1
while i < 12:
    for j in range(n):
        b=float(mat[i][j])
        soma+=b
#        print(b,end=' ')
        div+=1
#    print()
    i+=1
    n+=1
    j=0
if st=='S':
    print('%.1f'%soma)
elif st=='M':
    soma=soma/div
    print('%.1f'%soma)
