#7.	Numa empresa paga-se R$ 19,50 a hora e recolhe-se para o
#imposto de renda 10% dos salários acima de R$ 1500,00. Dado o número
#de horas trabalhadas por
#um funcionário, informar o valor do seu salário líquido.

horas=float(input('Digite o número de horas trabalhadas\n'))

sal= (horas*19.5)

if sal > 1500:
    salr= sal * 0.1
    s= sal-salr
    print('O salario real é de %.2f\n'%s)
else:
    print('O sálrio real sem imposto de renda é de %.2f\n'%sal)
