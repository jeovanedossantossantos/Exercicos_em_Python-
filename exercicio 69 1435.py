while True:
    n = int(input())
    
    if n == 0:
        break
    
    matriz = [ \
              [0 for elemento in range(n)]
                  for linha in range(n)
    ]
    
    indice = 0
    numero = 1
    
    while indice < n:
        for i in range(n):
            if i >= indice:
                matriz[indice][i] = numero
                matriz[i][indice] = numero
        indice += 1
        numero += 1
    offset = n - 1
    for i in range(n):
        for j in range(n):
            matriz[offset-j][offset-i] = matriz[i][j]
    for i in range(n):
        linha = ''
        for j in range(n):
            linha += '{:>3}'.format(str(matriz[i][j])) + ' '
        print(linha[:-1])
    print()
