
while True:
    
    try:
        l=input()
        lesma=list(map(int , input().split()))   
#    for t in range(l):
        maior=int(max(lesma))
        if maior < 10:
            print('1')
        elif maior >= 10 and maior < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break

'''
while True:
    try:
        n=int(input())
        if n == 0:
            print('vai ter copa!')
        elif n > 0:
            print('vai ter duas!')
    except EOFError:
        break'''

