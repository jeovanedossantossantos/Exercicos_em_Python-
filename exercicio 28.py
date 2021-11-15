#fibonacci
'''g=int(input())
ultimo=0
penultimo=0
atual=1
n=1
f=0
while n <= g:
    if n==1:
        
        print('0', end=' ')
            
   print(%i%atual, end=' ')
    if atual==0:
        atual=1
    penultimo = ultimo
    print('%i'%penultimo,end='')
    ultimo = atual
#    print('u ',ultimo)
    atual = ultimo + penultimo
#    print('a ',atual)
    n+=1'''
g=int(input())
ultimo=0
penultimo=0
atual=1
n=1
while n <= g:
    penultimo = ultimo
    print('%i'%penultimo,end='')
    ultimo = atual
    atual = ultimo + penultimo
    n+=1
