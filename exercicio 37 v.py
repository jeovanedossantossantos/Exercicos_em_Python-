par = []
impar = []
for eu in  range(15):
    va =  int(input())
    if va %  2  ==  0:
        par.append(va)
    else :
        impar.append(va)
    
    if len (par) == 5:
        i =  0
        for v in par:
            print ("par[%d] = %d"%(i, v))
            i +=  1
        par = []
    if len (impar) == 5:
        i =  0
        for v in impar:
            print ("impar[%d] = %d"%(i, v))
            i +=  1
        impar = []
if len (impar) >  0:
    i =  0
    for v in impar:
        print ("impar[%d] = %d"%(i, v))
        i +=  1

if len (par) > 0:
    i =  0
    for v in par:
        print ("par[%d] = %d"%(i, v))
        i +=  1
        '''
par=[]
impar=[]

for j in range(15):
    va=int(input())
    if va % 2 == 0:
        par.append(va)
    else:
        impar.append(va)
    if len(par) == 5:
        t=0
        for b in par:
            print('par[%d] = %d'%(t,b))
            t+=1
        par=[]
    if len(impar)==5:
        t=0
        for b in impar:
            print('impar[%d] = %d'%(t,b))
            t+=1
        impar=[]
if len(impar)>0:
    t=0
    for b in impar:
        print('impar[%d] = %d'%(t,b))
        t+=1
if len(par)>0:
    t=0
    for b in impar:
        print('par[%d] = %d'%(t,b))
        t+=1'''
