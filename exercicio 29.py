#media das idades
idade=0
media=0
n=0
while idade >= 0:
    idade=int(input())
    if idade >= 0:
        media=(media+idade)
        n+=1
media=media/n
print('%.2f'%media)
    
