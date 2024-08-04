#include <stdio.h>
#include <locale.h>

int main()
{
int N,digito=0,div=1,cont=0,i;
printf("digite um valor ");
scanf("%d",&N);
  int vetor[N];
  while(N!=0){
    digito=N%10;
    vetor[cont]=digito;
    cont++;
    N/=10;
  }
for(i=cont-1;i>=0;i--){
  printf("%d \n", vetor[i]);
}

  return 0;
}

