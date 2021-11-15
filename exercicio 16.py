#6.	Modifique a questão anterior, caso os lados formem um triângulo,
#encontre e imprima  o seu tipo:
 #   Equilátero, isósceles ou escaleno.

a=float(input('Digite o 1° número\n'))
b=float(input('Digite o 2° número\n'))
c=float(input('Digite o 3° número\n'))

if a != 0 and b != 0 and c !=0:
    print('É um triangulo\n')
    if a == b and a == c and c == b:
        print('Triângulo Equilátero\n')
    elif a != b and b != c and c != a:
        print('Triângulo Escaleno\n')
    else:
        print('Triângulo Isósceles\n')
else:
    print('Não é um triangulo\n')
