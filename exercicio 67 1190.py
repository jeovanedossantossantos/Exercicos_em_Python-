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
j=11
n=6
h=1
while n < j:
    while i < j:
        b=float(mat[i][j])
        soma+=b
        div+=1
        i+=1
#        print(b,end=' ')
#    print()
    h+=1
    i=h
    j-=1
if st=='S':
    print('%.1f'%soma)
elif st=='M':
    soma=soma/div
    print('%.1f'%soma)
