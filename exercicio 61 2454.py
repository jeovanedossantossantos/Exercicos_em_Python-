n=input().split()
p=int(n[0])
r=int(n[1])

if p == 0:
    print('C')
elif p == 1 and r == 0:
    print('B')
elif p == 1 and r == 1:
    print('A')
