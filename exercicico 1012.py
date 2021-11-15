valor=input().split()
a=float(valor[0])
b=float(valor[1])
c=float(valor[2])
tri = (a*c)/2
cir = (c**2 * 3.14159)
tra = (a + b) * c/2
qua = b**2
ret = a * b
print('TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f'%(tri,cir,tra,qua,ret))
