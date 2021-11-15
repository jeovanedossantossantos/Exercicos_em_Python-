x=float(input())
lista=[]
for i in range(100):
    lista.append(x)
    print('N[%i] = %.4f'%(i,lista[i]))
    x=x/2
