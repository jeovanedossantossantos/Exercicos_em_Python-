pa=input().split()

x=float(pa[0])
y=float(pa[1])

if x==0 and y==0:
    print('Origrm')
elif x!=0 and y==0:
    print('Eixo X')
elif x==0 and y!=0:
    print('Eixo Y')
elif x>=0 and y>0:
    print('Q1')
elif x<0 and y>=0:
    print('Q2')
elif x<0 and y<0:
    print('Q3')
else:
    print('Q4')
