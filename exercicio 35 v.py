n=int(input())
lista=list(map(int,input().split()))

#t=21
t=lista[0]
i=1

for indice,numero in enumerate(lista):
    if numero < t:
        t=numero
        i=indice +1
    

print(i)
'''#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main(){
	short n, resp, i = 1, t, posicMenor = 21;
	
	scanf("%hd", &n);
	
	while(i <= n){
		scanf("%hd", &t);
		if(t < posicMenor){ posicMenor = t; resp = i;}
		i++;
	}
	
	printf("%hd\n", resp);
	
	return 0;
'''

    
    
