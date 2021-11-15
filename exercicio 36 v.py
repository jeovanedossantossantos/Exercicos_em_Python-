q=int(input ())
lis=list( map ( int , input().split()))

onde=  0
pequeno =lis [ 0 ]
cont =  0
for mud in lis:
    if mud < pequeno:
        pequeno = mud
        onde = cont
    cont += 1
    
print("Menor valor: %d"%pequeno)
print("Posicao: %d"%onde)

