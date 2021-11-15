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
#mat[11][11]
n=11
i=11
j=11
q=0
for q in range(11):
    for f in range(n):
        b=float(mat[i][j])
        soma+=b
#        print(b,end=' ')
        j-=1
        div+=1
#    print()
    i-=1
    j=11
    n-=1
    
if st=='S':
    print('%.1f'%soma)
elif st=='M':
    soma=soma/div
    print('%.1f'%soma)
