#2.	Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

l=str(input('Digite [F] para feminino e [M] para masculino\n'))


if l=='F':
    print('{} - Feminino\n'.format(l))
elif l=='M':
    print('{} - Masculino\n'.format(l))
else:
    print('{} - Sexo invalido\n')
