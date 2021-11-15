'''lista=[]
maior=0
posição=0
for i in range(10):
    valor=int(input())
    lista.append(valor)
    if maior <= int(lista[i]):
        maior=int(lista[i])
        posição=i
print(maior)
print(posição+1)'''
'''v1=int(input())
v2=int(input())
if v2 < v1:
    v=v2
    v2=v1
    v1=v
soma=0
while v1 <= v2:
    if v1 % 13 != 0:
      soma=soma+v1
    v1+=1
print(soma)'''
nume=int(input())
while nume != 0:
    i=1
    soma=''
    while i <= nume:
        soma+=str(i) + ' '
        i+=1
    print(soma[:-1])
    nume=int(input())
    
        
        
