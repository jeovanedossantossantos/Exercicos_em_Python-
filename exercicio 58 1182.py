mat=[]
linha=[]
n=int(input())
st=input()
for i in range(12):
    for j in range(12):
        ve=float(input())
        linha.append(ve)
    mat.append(linha)
    linha=[]
soma=0
if st == 'S':
    for i in range(12):
        b=float(mat[i][n])
        soma+=b
elif st == 'M':
    for i in range(12):
        b=float(mat[i][n])
        soma=soma+b
    soma=soma/12
print('%.1f'%soma)
