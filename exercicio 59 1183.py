'''mat=[]
linha=[]
soma=0
st=input()
#C=1
#valor=0
for i in range(12):
    j=0
    for j in range(12):
        valor=float(input())
#        valor+=C
        linha.append(valor)
#        print(valor)
    mat.append(linha)
    linha=[]
cont=1
j=1
for i in range(12):
    for j in range(12):
        b=float(mat[i][j])
        soma+=b
#        print(b,end=' ')
#    print()
    cont+=1
    j=cont
if st=='S' or st=='s':
    print('%.1f'%soma)
elif st=='M' or st=='m':
    soma=soma/i
    print('%.1f'%soma)'''
'''op = input()
soma = 0
c_out = 1
c_in = 11
qte = 0
nao_entra = c_out
entra = c_in
valor=0

for i in range(144):
#	valor = float(input())
    valor+=1
    if nao_entra + entra == 0:
        c_out += 1
        c_in -= 1
        nao_entra = c_out
        entra = c_in

    if (nao_entra > 0):
        nao_entra -= 1
        continue
	
    if (entra > 0):
        entra -= 1
        soma += valor
        qte += 1
        continue
		
if(op == 'S'):
	print('%.1f' %soma)
else:
	print('%.1f' %(soma/float(qte)))
'''
mat=[]
linha=[]
soma=0
st=input()
C=1
valor=0
for i in range(12):
    j=0
    for j in range(12):
#        valor=float(input())
        valor+=C
        linha.append(valor)
        print(valor,end=' ')
    print()
    mat.append(linha)
    linha=[]
cont=1
j=1
print()
div=0
for i in range(12):
    while j < 12:
        b=float(mat[i][j])
        soma+=b
        print(b,end=' ')
        j+=1
        div+=1
    print()
    cont+=1
    j=cont
if st=='S' or st=='s':
    print('%.1f'%soma)
elif st=='M' or st=='m':
    soma=soma/div
    print('%.1f'%soma)

