'''str=input()
print(str.count(' '))'''

'''a=input().lower()
b=input().lower()
if a == b:
    print(' iguais')
else:
    print('diferentes')'''
n=int(input())
for i in range(n):
    str1,str2=input().split()
    quat2=len(str2)
    if quat2 > len(str1):
        print('nao encaixa')
    else:
        novastr1=str1[-quat2:]
        if novastr1 == str2:
            print('encaixa')
        else:
            print('nao encaixa')

