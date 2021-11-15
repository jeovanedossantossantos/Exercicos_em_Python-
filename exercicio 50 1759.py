n=int(input())
soma=''
for i in range(n):
    soma+= 'Ho'+' '
soma=(soma[:-1])
i+=1
if i == n:
    soma+= '!'
print(soma)
