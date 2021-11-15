#b > 0 or b < 0 q=[a/b] e r = a -b*q
vetor=input().split()
a=int(vetor[0])
b=int(vetor[1])

if (b != 0) and (a > 0):
    q = int(a/b)
    r = a - b * q

    print('%i %i'%(q,r))
else:
    d=a+1
    c=b-1
    q = int(d/c)
    r = a - b * q

    print('%i %i'%(q,r))
