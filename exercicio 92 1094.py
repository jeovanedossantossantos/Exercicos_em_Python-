n = int(input())
lista=[]
t=0
j=0
cobaias=0
coelho=0
ratos=0
sapos=0
for i in range(n):
    lista.append(input().split())
    it=int(lista[t][0])
    st=str(lista[j][1])
    t+=1
    j+=1
    if st == 'C':
        coelho+=it
    elif st == 'R':
        ratos+=it
    elif st == 'S':
        sapos+=it
    cobaias+=it
pc=(coelho * 100)/cobaias
pr=(ratos * 100)/cobaias
ps=(sapos * 100)/cobaias
s='%'
print('Total: %i cobaias'%cobaias)
print('Total de coelhos: %i'%coelho)
print('Total de ratos: %i'%ratos)
print('Total de sapos: %i'%sapos)
print('Percentual de coelhos: %.2f %s'%(pc,s))
print('Percentual de ratos: %.2f %s'%(pr,s))
print('Percentual de sapos: %.2f %s'%(ps,s))
