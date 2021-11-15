#3.	Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#•	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#•	A mensagem "Reprovado", se a média for menor do que sete;
#•	A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota=input('Digite as duas notas\n').split()

nota1=float(nota[0])
nota2=float(nota[1])

media=(nota1+nota2)/2
if media >= 7 and media < 10:
    print('Aprovado\n')
elif media == 10:
    print('Aprovado com Distinção\n')
else:
    print('Reprovado\n')
