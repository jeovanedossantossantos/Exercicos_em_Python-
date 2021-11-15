'''Na matemática, um Número Primo é aquele que pode ser dividido somente
por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser
dividido apenas pelo número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém
um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada.
Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107),
que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou
“X nao eh primo”, de acordo com a especificação fornecida.'''

n=int(input())

for linha in range(n):
    numero = int(input())
    div = 2
    primo = True
    while div < numero:
        if numero % div == 0:
            primo = False
            break
        div  += 1
    if primo:
        print('%i eh primo'%numero)
    else:
        print('%i nao eh primo'%numero)
