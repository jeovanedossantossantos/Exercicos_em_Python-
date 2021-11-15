n=int(input())
for i in range(n):
    palavra=input()
    soma=''
    if i == 0:
        for i in range(len(palavra)):
            a=ord(palavra[i])
            if (ord('z') >= a >= ord('a')) and (ord('A') <= a <= ord('Z')):
                a = chr(a + 3)
            soma+=a
            n=1
            soma2=''
        for i in range(len(palavra)):
            a=soma[len(palavra)-n)
            n+=1
            soma2+=a
        numero=len(palavra)/2
        for i in range(numero):
            
