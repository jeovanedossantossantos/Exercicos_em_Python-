'''n = int(input())
x = 0
intervalo = 0
fora = 0

for k in range(0, n, 1):
    x = int(input())

    if x >= 10 and x <= 20:
        intervalo += 1
    else:
        fora += 1

print("%s in" %intervalo)
print("%s out" %fora)'''


n=int(input())
i=0
out=0
v=0
while i<n:
    i=i+1
    x=int(input())
        
    if x<=10 or x>=20:
        out=out+1
    if x>10 and x<20:
        v=v+1
print('{} in'.format(v))
print('{} out'.format(out))


