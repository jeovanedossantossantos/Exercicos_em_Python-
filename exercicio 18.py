#8.	Dados os coeficientes ( a≠0, b e c ) de uma equação do 2° grau,
#calcule e informe suas raízes reais, usando a fórmula de Báskara.

a=float(input('Digite o termo de A diferente de zero\n'))
b=float(input('Digite o termo de B\n'))
c=float(input('Digite o termo de C\n'))

if a!=0:
    delta =(b**2-4*a*c)

    if delta >= 0:
        xl=((-1*b-(b**2-(4*a*c))**0.5))/2*a
        xm=((-1*b+(b**2-(4*a*c))**0.5))/2*a

        if xl==0:
            xl=xl * -1
        if xm==0:
            xm= xm * -1
            
       # print('As raizes são {} e {}'.format(xl,xm))
        print('As raizes são %.2f e %.2f '%(xl,xm))

    else:
        print('Ipossivel resolver esta equação\n')
else:
    print('Valor de A é invalido\n')

'''a=int(input(''))
b=int(input(''))
if a==0:
#c= a * b
    print('sim')
else:
    print('sd')'''
