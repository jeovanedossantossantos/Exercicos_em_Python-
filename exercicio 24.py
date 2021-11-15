'''Leia a hora inicial e a hora final de um jogo.
A seguir calcule a duração do jogo, sabendo que o mesmo
pode começar em um dia e terminar em outro, tendo uma duração
mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando
a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixh1'''


horas=input().split()

i=int(horas[0])
g=int(horas[1])

if i<g:
    d=g-i
elif i>g:
    d=(24-i)+g
else:
    d=24
print('O JOGO DUROU %i HORA(S)'%d)

'''horas=input().split()

i=int(horas[0])
g=int(horas[1])

if i<g:
    d=g-i
elif i>g:
    d=(24-i)+g
else:
    d=24
print('O JOGO DUROU %i HORA(S)'%d)'''
