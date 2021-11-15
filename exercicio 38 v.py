tabela = [ 0 , 1 ]
anterior = 0
atual = 1

for eu in  range( 60 ):
    tnp = atual + anterior
    tabela.append (tnp)
    anterior = atual
    atual = tnp

qte =  int ( input ())
for eu in  range(qte):
    valor =  int ( input ())
    print ('Fib(%d) = %d'%(valor, tabela [valor]))
