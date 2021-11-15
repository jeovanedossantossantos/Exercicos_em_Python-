salrio=float(input())

if salrio<=400:
    reaj=salrio*0.15
    salrio=salrio+reaj
    p=15
elif salrio<=800:
    reaj=salrio*0.12
    salrio=salrio+reaj
    p=12
elif salrio<=1200:
    reaj=salrio*0.10
    salrio=salrio+reaj
    p=10
elif salrio<=2000:
    reaj=salrio*0.07
    salrio=salrio+reaj
    p=7                 
else:
    reaj=salrio*0.04
    salrio=salrio+reaj
    p=4

print('Novo salario: %.2f'%salrio)
print('Reajuste ganho: %.2f'%reaj)
print('Em percentual: {} %'.format(p))
