#7.	Faça um programa que peça o tamanho
#de um arquivo para download (em MB) e a velocidade de
#um link de Internet (em Mbps), calcule e informe o tempo aproximado
#de download do arquivo usando este link (em minutos)

mb=float(input('Digite o tamanho do arquivo em MB\n'))
mbps=float(input('Digite a velocidade do link em Mbps\n'))

#v=s/t
#s=v*t
#t=s/v

t=mb/mbps
tempo=t/60
print('O tmpo gasto nesse dawload sera de:%.2f minutos\n'%tempo)
