'''n=int(input())
lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lis=[]
for i in range(n):
    s=input()
    num=int(input())
    tam=len(s)
    lis.append()
    #2-6=-4'''
'''quantidade=int(input())
for i in range(quantidade):
    palavra=input()
    n=int(input())
    lista=[]
    for letra in palavra:
        nova=ord(letra)-n
        if nova<65:
            
            novaletra=chr(nova)
            lista.append(novaletra)


    print(''.join(lista))'''
n=int(input())
for i in range(n):
    s=input()
    t=int(input())
    soma=''
    for j in range(len(s)):
        b=ord(s[j])
        print(b,end='')
        nova=26-t
        non=nova+b
        if non > 90:
            non=b-t
        non=chr(non)
        soma+= non
    print(soma)
        
